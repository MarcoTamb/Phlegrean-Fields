import requests
from datetime import date
import pandas as pd
from io import StringIO
from geopy import distance
from utils.constants import MIN_DATE, LATITUDE, LONGITUDE, MAX_DISTANCE_KM
from utils.cache import cache

start_date = date.today() - MIN_DATE


def get_y(coordinates):
    if float(coordinates[0]) > float(LATITUDE):
        return distance.distance(coordinates, (LATITUDE, coordinates[1])).kilometers
    else:
        return - distance.distance(coordinates, (LATITUDE, coordinates[1])).kilometers


def get_x(coordinates):
    if float(coordinates[1]) > float(LONGITUDE):
        return distance.distance(coordinates, (coordinates[0], LONGITUDE)).kilometers
    else:
        return - distance.distance(coordinates, (coordinates[0], LONGITUDE)).kilometers


# This decorator implements a 1-hour rate-limit automatically
@cache.memoize()
def get_earthquake_data():
    print("Fetching fresh data from INGV...")
    try:
        query = f'https://webservices.ingv.it/fdsnws/event/1/query?starttime={start_date.strftime("%Y-%m-%d")}T00%3A00%3A00&endtime={date.today().strftime("%Y-%m-%d")}T23%3A59%3A59&minmag=-1&maxmag=10&mindepth=-10&maxdepth=1000&orderby=time-asc&lat={LATITUDE}&lon={LONGITUDE}&maxradiuskm={MAX_DISTANCE_KM}&format=text'
        data_query = requests.get(query, timeout=20)
        data_query.raise_for_status()  # Raises an error for 404, 500 status codes
        df = pd.read_csv(StringIO(data_query.text), sep='|', parse_dates=['Time'])
    except Exception as e:
        print(f"INGV API fetch failed: {e}")  # print exception in log
        df = pd.read_csv('query.csv', sep='|', parse_dates=['Time'])

    df['Depth/Km'] = -df['Depth/Km']
    df['latitude_longitude'] = list(zip(df.Latitude, df.Longitude))
    df['x_position'] = df['latitude_longitude'].apply(get_x)
    df['y_position'] = df['latitude_longitude'].apply(get_y)

    return df


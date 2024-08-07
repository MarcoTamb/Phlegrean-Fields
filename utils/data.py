import requests
from datetime import date, datetime, timedelta
import pandas as pd
from io import StringIO
from geopy import distance
from utils.constants import MIN_DATE, LATITUDE, LONGITUDE, MAX_DISTANCE_KM
from dash import callback, Input, Output

start_date = date.today() - MIN_DATE

rate_limit_delay=600
last_query=datetime.now()-(timedelta(seconds=rate_limit_delay+5))
print(last_query.strftime("%m %d %H-%M-%S"))


def query_earthquakes():
    print("update")
    try:
        query=f'https://webservices.ingv.it/fdsnws/event/1/query?starttime={start_date.strftime("%Y-%m-%d")}T00%3A00%3A00&endtime={date.today().strftime("%Y-%m-%d")}T23%3A59%3A59&minmag=-1&maxmag=10&mindepth=-10&maxdepth=1000&orderby=time-asc&lat={LATITUDE}&lon={LONGITUDE}&maxradiuskm={MAX_DISTANCE_KM}&format=text' 
        data_query=requests.get(query)
        phlegrean_fields_earthquakes = pd.read_csv(StringIO(data_query.text), sep='|', parse_dates=['Time'])
    except:
        phlegrean_fields_earthquakes=pd.read_csv('query.csv', sep='|', parse_dates=['Time'])
    return phlegrean_fields_earthquakes

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

earthquake_data=query_earthquakes()
earthquake_data['Depth/Km']=-earthquake_data['Depth/Km']
earthquake_data['latitude_longitude'] = list(zip(earthquake_data.Latitude, earthquake_data.Longitude)) 
earthquake_data['x_position'] = earthquake_data['latitude_longitude'].apply(get_x)
earthquake_data['y_position'] = earthquake_data['latitude_longitude'].apply(get_y)


@callback(
    Output('refresh', 'data'),
    Input('update-data', 'n_intervals')
)
def update_data(interval):
    global earthquake_data
    global last_query
    print((datetime.now()-last_query).seconds)
    if (datetime.now()-last_query).seconds>rate_limit_delay:
        earthquake_data=query_earthquakes()
        earthquake_data['Depth/Km']=-earthquake_data['Depth/Km']
        earthquake_data['latitude_longitude'] = list(zip(earthquake_data.Latitude, earthquake_data.Longitude)) 
        earthquake_data['x_position'] = earthquake_data['latitude_longitude'].apply(get_x)
        earthquake_data['y_position'] = earthquake_data['latitude_longitude'].apply(get_y)
        last_query=datetime.now()
    else:
        print("did not update")
    return interval
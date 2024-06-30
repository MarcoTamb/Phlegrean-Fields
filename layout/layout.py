from dash import html, callback, Output, Input, State, page_container, dcc
import dash_bootstrap_components as dbc
from utils.constants import URL_MAIN, GITHUB_URL, PLOTLY_LOGO, MIN_DATE, LATITUDE, LONGITUDE, MAX_DISTANCE_KM, UPDATE_SECONDS, APP_TITLE
from datetime import date

start_date = date.today() - MIN_DATE 

INGV_url=f'https://terremoti.ingv.it/events?starttime={start_date.strftime("%Y-%m-%d")}T00%3A00%3A00&endtime={date.today().strftime("%Y-%m-%d")}T23%3A59%3A59&minmag=-1&maxmag=10&mindepth=-10&maxdepth=1000&minversion=100&orderby=time-asc&lat={LATITUDE}&lon={LONGITUDE}&maxradiuskm={MAX_DISTANCE_KM}&format=text&limit=10000'

links=[
        dbc.NavItem(dbc.NavLink(
                "Maps",
                href='/',
                className='links'
             )),
        dbc.NavItem(dbc.NavLink(
                "Statistics",
                href='/stats',
                className='links'
             )),
        dbc.NavItem(dbc.NavLink(
            "About",
            href='/about',
            className='links'
        )),
        dbc.DropdownMenu(
            children=[
                dbc.DropdownMenuItem("INGV websites", header=True),
                dbc.DropdownMenuItem("INGV Home", href='https://www.ingv.it/'),
                dbc.DropdownMenuItem("INGV Earthquakes", href=INGV_url),
                dbc.DropdownMenuItem("INGV Monitoring", href='https://www.ov.ingv.it/index.php/monitoraggio-e-infrastrutture/bollettini-tutti'),
            ],
            nav=True,
            in_navbar=True,
            label=html.Span("INGV", style={'color':'var(--bs-nav-link-color)'}),
            className='links'
        ),
        dbc.NavItem(dbc.NavLink(
                "GitHub",
                href=GITHUB_URL,
                className='links'
             )),
      ]
# I will probably add a couple of pages to explain the data. In that case this goes in a separate page layout


app_layout = html.Div(
        [
            dbc.NavbarSimple(
                children=links,
                brand=[html.Img(src=PLOTLY_LOGO, height="30px"), dbc.NavbarBrand(APP_TITLE, className="ms-2")],
                brand_href= '/',
                color="dark",
                dark=True,
            ), 
            page_container, 
            dcc.Interval(
                id='update-data',
                interval=UPDATE_SECONDS*1000, # in milliseconds
                n_intervals=0
            ),
            dcc.Store(id='refresh', data=[])
        ],
        className='page'
    )



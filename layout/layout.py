from dash import html, callback, Output, Input, State, page_container, dcc
import dash_bootstrap_components as dbc
from utils.constants import URL_MAIN, GITHUB_URL, PLOTLY_LOGO, MIN_DATE, LATITUDE, LONGITUDE, MAX_DISTANCE_KM, UPDATE_SECONDS
from datetime import date

INGV_url=f'https://terremoti.ingv.it/events?starttime={MIN_DATE.strftime("%Y-%m-%d")}T00%3A00%3A00&endtime={date.today().strftime("%Y-%m-%d")}T23%3A59%3A59&minmag=-1&maxmag=10&mindepth=-10&maxdepth=1000&minversion=100&orderby=time-asc&lat={LATITUDE}&lon={LONGITUDE}&maxradiuskm={MAX_DISTANCE_KM}&format=text&limit=10000'

links=[
        html.A(
                "Charts",
                href='/',
                className='links'
             ),
        html.A(
            "About",
            href='/about',
            className='links'
        ),
        html.A(
            "INGV home",
            href='https://www.ingv.it/',
            className='links'
        ),
        html.A(
            "INGV earthquakes",
            href=INGV_url,
            className='links'
        ),
        html.A(
            "INGV monitoring",
            href='https://www.ov.ingv.it/index.php/monitoraggio-e-infrastrutture/bollettini-tutti',
            className='links'
        ),
        html.A(
                "GitHub",
                href=GITHUB_URL,
                className='links'
             ),
      ]
# I will probably add a couple of pages to explain the data. In that case this goes in a separate page layout


app_layout = html.Div(
        [
            dbc.Navbar(
                dbc.Container(
                    [
                        html.A(
                            # Use row and col to control vertical alignment of logo / brand
                            dbc.Row(
                                [
                                    dbc.Col(html.Img(src=PLOTLY_LOGO, height="30px")),
                                    dbc.Col(dbc.NavbarBrand("Phlegrean Fields Earthquakes", className="ms-2")),
                                ],
                                align="center",
                                className="g-0",
                            ),
                            href=URL_MAIN,
                            style={"textDecoration": "none"},
                        ),
                        dbc.NavbarToggler(id="navbar-toggler", n_clicks=0),
                        dbc.Collapse(
                            links,
                            id="navbar-collapse",
                            is_open=False,
                            navbar=True,
                        ),
                    ]
                ),
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



# add callback for toggling the collapse on small screens
@callback(
    Output("navbar-collapse", "is_open"),
    Input("navbar-toggler", "n_clicks"),
    State("navbar-collapse", "is_open"),
)
def toggle_navbar_collapse(n, is_open):
    if n:
        return not is_open
    return is_open
from dash import html, callback, Input, Output
import dash_mantine_components as dmc
from utils.constants import MIN_DATE
from datetime import date, timedelta

controls=html.Div([
    dmc.SegmentedControl(
            id="chart-type",
            data=['Dates', 'Time-delta', 'Magnitude', 'Depth'],
            value='Dates',
            fullWidth=True
        ),
    html.P(),
    html.H5("Dates:"),
    dmc.RangeSlider(id="date-stats",
               value=[0, MIN_DATE.days], 
               min=0, 
               max=MIN_DATE.days, 
               step=1, 
               minRange=90,
               className='slider_shortbottom'
        ),
    html.P(id='first-date-text-stats', children='First:'),
    html.P(id='last-date-text-stats', children='Last:'),
    html.H5("Minimum Magnitude:"),
    dmc.Slider(id='min-magnitudo-stats', 
               value=0, 
               min=0, 
               max=4, 
               marks=[
                {"value": 0, "label": "0"},
                {"value": 1, "label": "1"},
                {"value": 2, "label": "2"},
                {"value": 3, "label": "3"},
                {"value": 4, "label": "4"},
            ],
            step=0.1, 
            className='slider'
            #tooltip={"template": "minimum magnitudo {value}", "placement": "top", "always_visible": False}
        ),
    html.P(),
    html.H5("Depth (km):"),
    dmc.RangeSlider(id="depth-km-stats",
               min=-7.5, 
               max=0, 
               step=0.1, 
               value=[-7.5, 0], 
               minRange=0.5,
               className='slider'
        ),
], className='controlsbox')

@callback(
    Output('first-date-text-stats', 'children'),
    Output('last-date-text-stats', 'children'),
    Input('date-stats', 'value'),
)
def update_date(slider_value):
    first_date=((date.today() - MIN_DATE)+timedelta(days=slider_value[0])).strftime('%Y-%m-%d')
    last_date=((date.today() - MIN_DATE)+timedelta(days=slider_value[1])).strftime('%Y-%m-%d')
    return f'First: {first_date}', f'Last: {last_date}'


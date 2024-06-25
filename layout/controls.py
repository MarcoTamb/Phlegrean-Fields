from dash import html, callback, Input, Output
import dash_mantine_components as dmc
from utils.constants import MIN_DATE
from datetime import date, timedelta
max_days=int((date.today()-MIN_DATE).days)
controls=html.Div([
    # html.H5("Map Type:"),
    dmc.SegmentedControl(
            id="map-type",
            data=['3D-Map', 'Heatmap', 'Vertical X', 'Vertical Y'],
            value='3D-Map',
            fullWidth=True
        ),
    html.P(),
    html.H5("Filter out older than:"),
    dmc.RangeSlider(id="last-date",
               value=[max_days-365, max_days], 
               min=0, 
               max=max_days, 
               step=1, 
               minRange=7,
               updatemode = 'drag',
        ),
    html.P(id='first-date-text', children='First date'),
    html.P(id='last-date-text', children='Last date'),
    html.H5("Minimum Magnitudo:"),
    dmc.Slider(id='min-magnitudo', 
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
            updatemode = 'drag',
            #tooltip={"template": "minimum magnitudo {value}", "placement": "top", "always_visible": False}
        ),
    html.P(),
    html.H5("Depth (km):"),
    dmc.RangeSlider(id="depth-km",
               min=-7.5, 
               max=0, 
               step=0.1, 
               value=[-7.5, 0], 
               minRange=0.5,
               updatemode = 'drag',
        ),
], className='controlsbox')

@callback(
    Output('first-date-text', 'children'),
    Output('last-date-text', 'children'),
    Input('last-date', 'value'),
)
def update_date(slider_value):
    first_date=(MIN_DATE+timedelta(days=slider_value[0])).strftime('%Y-%m-%d')
    last_date=(MIN_DATE+timedelta(days=slider_value[1])).strftime('%Y-%m-%d')
    return f'First date :{first_date}', f'Last date :{last_date}'
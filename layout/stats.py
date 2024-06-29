from dash import dcc, html, callback, Output, Input
import plotly.express as px
import pandas as pd
from utils.data import earthquake_data, LATITUDE, LONGITUDE
from utils.constants import MIN_DATE
import plotly.graph_objects as go
import numpy as np
from skimage import io
from skimage.color import rgb2gray
from skimage.transform import rescale
from datetime import timedelta, date

x_axis_range=[10,-10]
y_axis_range=[10,-10]

# create trace for the map of the area
original = io.imread('assets/map.png')[:,:,:3] #https://github.com/empet/Datasets/blob/master/Images/mountains.jpg
img=rgb2gray(original)
img=rescale(img, 0.7, anti_aliasing=True)

xx = np.linspace(y_axis_range[0], y_axis_range[1], img.shape[1])
yy = np.linspace(x_axis_range[0], x_axis_range[1], img.shape[0])
zz = np.zeros(img.shape[:2])
pl_grey =[[0.0, 'rgb(0, 0, 0)'],
    [0.05, 'rgb(13, 13, 13)'],
    [0.1, 'rgb(29, 29, 29)'],
    [0.15, 'rgb(45, 45, 45)'],
    [0.2, 'rgb(64, 64, 64)'],
    [0.25, 'rgb(82, 82, 82)'],
    [0.3, 'rgb(94, 94, 94)'],
    [0.35, 'rgb(108, 108, 108)'],
    [0.4, 'rgb(122, 122, 122)'],
    [0.45, 'rgb(136, 136, 136)'],
    [0.5, 'rgb(150, 150, 150)'],
    [0.55, 'rgb(165, 165, 165)'],
    [0.6, 'rgb(181, 181, 181)'],
    [0.65, 'rgb(194, 194, 194)'],
    [0.7, 'rgb(206, 206, 206)'],
    [0.75, 'rgb(217, 217, 217)'],
    [0.8, 'rgb(226, 226, 226)'],
    [0.85, 'rgb(235, 235, 235)'],
    [0.9, 'rgb(243, 243, 243)'],
    [0.95, 'rgb(249, 249, 249)'],
    [1.0, 'rgb(255, 255, 255)']]

surfcolor = np.fliplr(img)
map_trace=go.Surface(go.Surface(x=xx, 
                                y=yy, 
                                z=zz, 
                                surfacecolor=surfcolor, 
                                colorscale=pl_grey, 
                                showscale=False, 
                                opacity = 0.6,
                                hovertemplate = 'E/W offset (km): %{x}<br>N/S offset (km): %{y}<br>%Depth (km): %{z}<extra></extra>'
                                ))
# default blank page
blank = go.Figure(go.Scatter(x=[], y = []))
blank.update_layout(template = None)
blank.update_xaxes(showgrid = False, showticklabels = False, zeroline=False)
blank.update_yaxes(showgrid = False, showticklabels = False, zeroline=False)
blank.update_layout({
            'plot_bgcolor': 'rgba(0, 0, 0, 0)',
            'paper_bgcolor': 'rgba(0, 0, 0, 0)',
        })


stats_wrapper = html.Div( 
    [
        html.H6(id='description-stats', className='chart-title'),
        html.Div(
            dcc.Graph(
                id='chart',
                figure=blank,
                className='main-chart'
            ),
        )
    ]
)



@callback(
    Output(component_id='chart', component_property='figure' ),
    Input(component_id='chart-type', component_property='value'),
    Input(component_id='min-magnitudo-stats', component_property='value'),
    Input(component_id='date-stats', component_property='value'),
    Input(component_id='depth-km-stats', component_property='value'),
    Input('refresh', 'data'),
)
def update_chart(chart_type, min_magnitudo, last_date_slider, depth, refresh_data):
    first_date=(date.today() - MIN_DATE ) + timedelta(days=last_date_slider[0])
    last_date=(date.today() - MIN_DATE ) + timedelta(days=last_date_slider[1])
    chart_data = earthquake_data.copy()
    chart_data = chart_data[chart_data.Magnitude > min_magnitudo]
    chart_data = chart_data[chart_data.Time  > pd.to_datetime(first_date)]
    chart_data = chart_data[chart_data.Time  <= pd.to_datetime(last_date)]
    chart_data = chart_data[chart_data['Depth/Km']  > depth[0]]
    chart_data = chart_data[chart_data['Depth/Km']  <= depth[1]]
    
    if chart_type=='Dates':
        number_of_days=last_date_slider[1]-last_date_slider[0]
        if number_of_days < 20:
            nbins = number_of_days
        else:
            nbins = min(60, max(20, round(number_of_days/10)))
        chart = dates_chart(chart_data, nbins)
        chart.update_layout(
            uirevision=chart_type,
            font=dict(
                color="white"
            )
        )
        chart.update_layout({
            'plot_bgcolor': 'rgba(0, 0, 0, 0)',
            'paper_bgcolor': 'rgba(0, 0, 0, 0)',
        })
    elif chart_type=='Time-delta':
        chart_data['lags'] = (chart_data.Time - chart_data.Time.shift(1))/ np.timedelta64(1, 'h') 
        # chart_data['lags'] = np.clip(chart_data['lags'], a_min=0, a_max=200)
        chart = lags_chart(chart_data)
        chart.update_layout(
            uirevision=chart_type,
            font=dict(
                color="white"
            )
        )
        chart.update_layout({
            'plot_bgcolor': 'rgba(0, 0, 0, 0)',
            'paper_bgcolor': 'rgba(0, 0, 0, 0)',
        })
    elif chart_type=='Magnitude':

        chart = magnitude_chart(chart_data)
        chart.update_layout(
            uirevision=chart_type,
            font=dict(
                color="white"
            )
        )
        chart.update_layout({
            'plot_bgcolor': 'rgba(0, 0, 0, 0)',
            'paper_bgcolor': 'rgba(0, 0, 0, 0)',
        })
    elif chart_type=='Depth':
        chart = depth_chart(chart_data)
        chart.update_layout(
            uirevision=chart_type,
            font=dict(
                color="white"
            )
        )
        chart.update_layout({
            'plot_bgcolor': 'rgba(0, 0, 0, 0)',
            'paper_bgcolor': 'rgba(0, 0, 0, 0)',
        })
    else:
        chart = blank
    

    return chart
def dates_chart(chart_data, nbins):

    fig=px.histogram(chart_data, x='Time', nbins=nbins,  labels={
        'x_position':'E/W offset (km)', 'y_position':'N/S offset (km)', 'Depth/Km':'Depth (km)', 'Magnitude':'Magnitude', 'Time':'Time', '#EventID':'EventID',
    })
    fig.update_layout(bargap=0.2)
    fig.update_layout(
            margin=dict(r=0, l=0, b=0, t=0)
            )

    return fig
def lags_chart(chart_data):

    fig=px.histogram(chart_data[chart_data['lags'] <= 240], x='lags',  labels={
        'x_position':'E/W offset (km)', 'y_position':'N/S offset (km)', 'Depth/Km':'Depth (km)', 'Magnitude':'Magnitude', 'Time':'Time', '#EventID':'EventID', 'lags': 'Lag (hours)'
    })
    count_over=len(chart_data[chart_data['lags'] > 240])
    fig.add_trace(
        go.Bar(
            x=[240],
            y=[count_over],
            hovertemplate=f'Lag (hours)=>200<br>count={count_over}<extra></extra>',
            showlegend =False
        )
    )
    fig.update_layout(bargap=0.2)
    fig.update_layout(
            margin=dict(r=0, l=0, b=0, t=0)
            )

    return fig
def magnitude_chart(chart_data):

    fig=px.histogram(chart_data, x='Magnitude', labels={
        'x_position':'E/W offset (km)', 'y_position':'N/S offset (km)', 'Depth/Km':'Depth (km)', 'Magnitude':'Magnitude', 'Time':'Time', '#EventID':'EventID',
    })
    fig.update_layout(bargap=0.2)
    fig.update_layout(
            margin=dict(r=0, l=0, b=0, t=0)
            )

    return fig
def depth_chart(chart_data):

    fig=px.histogram(chart_data, x='Depth/Km', labels={
        'x_position':'E/W offset (km)', 'y_position':'N/S offset (km)', 'Depth/Km':'Depth (km)', 'Magnitude':'Magnitude', 'Time':'Time', '#EventID':'EventID',
    })
    fig.update_layout(bargap=0.2)
    fig.update_layout(
            margin=dict(r=0, l=0, b=0, t=0)
            )

    return fig

def heatmap(chart_data):
    fig = px.density_mapbox(chart_data, 
                            lat='Latitude', 
                            lon='Longitude', 
                            z='Magnitude', 
                            radius=10,
                            center=dict(
                                lat=float(LATITUDE), 
                                lon=float(LONGITUDE),
                                ), 
                            zoom=12,
                            mapbox_style="open-street-map",
                            labels={
                                'x_position':'E/W offset (km)', 
                                'y_position':'N/S offset (km)', 
                                'Depth/Km':'Depth (km)', 
                                'Magnitude':'Magnitude',
                                'Time':'Time', 
                                '#EventID':'EventID',
                            }, 
                            hover_data=["Time"]
                            )
    fig.update_layout(
        margin=dict(l=20, r=20, t=20, b=20),
    )
    return fig

def vertical(chart_data, axis_choice):
    if axis_choice=='E/W':
        x_element='x_position'
    elif axis_choice=='N/S':
        x_element='y_position'
    else:
        return []
    fig=px.scatter(chart_data, 
                   x=x_element, 
                   y='Depth/Km', 
                   size='Magnitude', 
                   color='Magnitude',
                   labels={
                        'x_position':'E/W offset (km)', 
                        'y_position':'N/S offset (km)', 
                        'Depth/Km':'Depth (km)', 
                        'Magnitude':'Magnitude',
                        'Time':'Time', 
                        '#EventID':'EventID',
                        }, 
                   hover_data=["Time"]
                   )
    fig.update_xaxes(range=[-6, 6])
    fig.update_yaxes(range=[-10, 0])
    fig.update_layout(
        margin=dict(l=20, r=20, t=20, b=20),
    )
    return fig 


@callback(
    Output('description-stats', 'children'),
    Input('chart-type', 'value'),
)
def update_description(type):
    if type=='Dates':
        return "Frequency of earthquakes over time"
    elif type=='Time-delta':
        return "Delay between consecutive earthquakes (hours)"
    elif type=='Magnitude':
        return "Distributions of the Magnitudes of earthquakes"
    elif type=='Depth':
        return "Distribution of earthquakes' depths"
    else:
        return 'This should never be displayed'
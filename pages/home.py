from dash import register_page, html, dcc
import dash_bootstrap_components as dbc
from layout.chart import chart_wrapper
from layout.controls import controls

register_page(__name__, path='/')

layout=html.Div(
    children=[
        html.Div(controls, className='controls'),
        html.Div(dcc.Loading(chart_wrapper), className='charts' ),
    ],
    className='gridbox',
    )


    # dbc.Row(
    #             [
    #                 dbc.Col(controls, md=3),
    #                 dbc.Col(dcc.Loading(chart_wrapper), md=7),
    #             ],
    #             align="center",
    #         )
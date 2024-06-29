from dash import register_page, html, dcc
import dash_bootstrap_components as dbc
from layout.stats import stats_wrapper
from layout.controls_stats import controls

register_page(__name__, path='/stats')

layout=html.Div(
    children=[
        html.Div(controls, className='controls'),
        html.Div(dcc.Loading(stats_wrapper), className='charts' ),
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
from layout.layout import app_layout
import dash_mantine_components as dmc
import dash_bootstrap_components as dbc
from dash import Dash

stylesheets = [
    "https://unpkg.com/@mantine/dates@7/styles.css",
    "https://unpkg.com/@mantine/code-highlight@7/styles.css",
    "https://unpkg.com/@mantine/charts@7/styles.css",
    "https://unpkg.com/@mantine/carousel@7/styles.css",
    "https://unpkg.com/@mantine/notifications@7/styles.css",
    "https://unpkg.com/@mantine/nprogress@7/styles.css",
    dbc.themes.DARKLY
]

app=Dash(__name__, external_stylesheets=stylesheets, use_pages=True)


app.layout=dmc.MantineProvider(
    theme = {},
    children = app_layout 
)
app.title = "Phlegraean Fields Earthquakes"
server=app.server

if __name__ == '__main__':
    print('Running app')
    app.run(debug=False)
import dash
from dash import html
import dash_bootstrap_components as dbc
import webbrowser

from threading import Timer
from components.cards import layout_tarjetas
from callbacks.filters import register_callbacks

external_stylesheets = [dbc.themes.DARKLY, "/assets/style.css"]

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
server = app.server

app.layout = dbc.Container(
    [
        html.H1(
            "Dashboard de Consultas Médicas 🩺📊",
            className="text-center mt-4 mb-4 text-light",
        ),
        layout_tarjetas,
    ],
    fluid=True,
)

register_callbacks(app)




def open_browser():
    webbrowser.open_new("http://127.0.0.1:8050/")

if __name__ == "__main__":
    Timer(1, open_browser).start()
    app.run(debug=False)

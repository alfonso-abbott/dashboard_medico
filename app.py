import os
import dash
from dash import html
import dash_bootstrap_components as dbc
from components.cards import kpi_cards, filter_controls, graph_tabs, mapa_component
from callbacks.filters import register_callbacks

external_stylesheets = [dbc.themes.CYBORG, "/assets/style.css"]

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
server = app.server

app.layout = dbc.Container([
    html.H1(
        "Dashboard de Consultas Médicas",
        className="text-center mt-4 mb-4 text-light",
    ),
    kpi_cards(),
    filter_controls(),
    graph_tabs(),
    mapa_component(),
], fluid=True)

register_callbacks(app)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8050))
    app.run_server(debug=False, host="0.0.0.0", port=port)


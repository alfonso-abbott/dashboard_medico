import dash
from dash import html
import dash_bootstrap_components as dbc

# Importamos los layouts de componentes visuales y filtros
from components.cards import layout_tarjetas
from callbacks.filters import register_callbacks

# Estilos visuales personalizados y tema bootstrap
external_stylesheets = [dbc.themes.DARKLY, "/assets/style.css"]

# Instanciamos la app Dash
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

# Requerido para despliegue en servidores como Heroku/Render
server = app.server

# Definimos el layout general de la aplicación
app.layout = dbc.Container([
    html.H1("Dashboard de Consultas Médicas 🩺📊", className="text-center mt-4 mb-4 text-light"),
    layout_tarjetas  # Tarjetas con KPIs y gráficos
], fluid=True)

# Registramos los callbacks definidos externamente
register_callbacks(app)

# Ejecutamos el servidor local solo si este archivo es el principal
if __name__ == "__main__":
    app.server(debug=True, port=8050)
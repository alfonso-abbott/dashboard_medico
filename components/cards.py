import dash_bootstrap_components as dbc
from dash import html, dcc
import plotly.express as px
from utils.funciones import (
    cargar_datos,
    total_consultas,
    especialidades_top,
    consultas_por_region,
    duracion_promedio,
    modalidad_consultas
)

# 🔹 Importar función para generar el mapa
from pathlib import Path
from maps.mapa_consultas import generar_mapa_consultas

# ✅ Aseguramos que el mapa se genere antes de insertarlo
mapa_file = Path("maps/mapa_output.html")
if not mapa_file.exists():
    generar_mapa_consultas()

# 🔄 Cargar datos una sola vez
df = cargar_datos()

# 📊 Gráfico: especialidades más consultadas
fig_especialidades = px.bar(
    especialidades_top(df),
    x=especialidades_top(df).index,
    y=especialidades_top(df).values,
    labels={"x": "Especialidad", "y": "Cantidad"},
    title="Especialidades más consultadas"
)

# 📈 Gráfico: modalidad presencial vs online
fig_modalidad = px.pie(
    modalidad_consultas(df),
    values=modalidad_consultas(df).values,
    names=modalidad_consultas(df).index,
    title="Distribución por modalidad"
)

# 🧱 Layout de tarjetas + gráficos
layout_tarjetas = dbc.Row([
    dbc.Col(dbc.Card([
        dbc.CardHeader("Consultas Totales"),
        dbc.CardBody(html.H4(f"{total_consultas(df)}", className="card-title"))
    ], color="primary", inverse=True), md=3),

    dbc.Col(dbc.Card([
        dbc.CardHeader("Duración Promedio (min)"),
        dbc.CardBody(html.H4(f"{duracion_promedio(df)}", className="card-title"))
    ], color="secondary", inverse=True), md=3),

    dbc.Col(dbc.Card([
        dbc.CardHeader("Gráfico: Modalidad"),
        dbc.CardBody(dcc.Graph(figure=fig_modalidad))
    ]), md=6),

    dbc.Col(dbc.Card([
        dbc.CardHeader("Gráfico: Especialidades Top"),
        dbc.CardBody(dcc.Graph(figure=fig_especialidades))
    ]), md=12),

    # 🗺️ Mapa embebido
    dbc.Col(dbc.Card([
        dbc.CardHeader("Mapa de Consultas"),
        dbc.CardBody(html.Iframe(
            id='mapa-consultas',
            srcDoc=mapa_file.read_text(encoding="utf-8"),
            width="100%",
            height="600",
            style={"border": "none"}
        ))
    ]), md=12)
], className="mb-4")

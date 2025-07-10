import dash_bootstrap_components as dbc
from dash import html, dcc
import plotly.express as px
from utils.funciones import (
    cargar_datos,
    total_consultas,
    duracion_promedio,
    especialidades_top,
    listar_regiones,
    listar_especialidades,
    listar_modalidades,
    listar_generos,
    rango_edad,
)
from maps.mapa_consultas import generar_mapa_consultas


df_base = cargar_datos()


def kpi_cards():
    df = df_base
    return dbc.Row([
        dbc.Col(dbc.Card([
            dbc.CardHeader("Consultas Totales"),
            dbc.CardBody(html.H4(total_consultas(df), className="card-title")),
        ], className="kpi-card"), md=3),
        dbc.Col(dbc.Card([
            dbc.CardHeader("Duración Promedio (min)"),
            dbc.CardBody(html.H4(duracion_promedio(df), className="card-title")),
        ], className="kpi-card"), md=3),
    ], className="mb-4")


def filter_controls():
    regiones = listar_regiones(df_base)
    modalidades = listar_modalidades(df_base)
    especialidades = listar_especialidades(df_base)
    generos = listar_generos(df_base)
    edad_min, edad_max = rango_edad(df_base)
    return dbc.Row([
        dbc.Col(dcc.Dropdown(id="dropdown-region", options=[{"label": r, "value": r} for r in regiones], placeholder="Región"), md=2),
        dbc.Col(dcc.Dropdown(id="dropdown-modalidad", options=[{"label": m, "value": m} for m in modalidades], placeholder="Modalidad"), md=2),
        dbc.Col(dcc.Dropdown(id="dropdown-especialidad", options=[{"label": e, "value": e} for e in especialidades], placeholder="Especialidad"), md=3),
        dbc.Col(dcc.Dropdown(id="dropdown-genero", options=[{"label": g, "value": g} for g in generos], placeholder="Género"), md=2),
        dbc.Col(dcc.RangeSlider(id="slider-edad", min=edad_min, max=edad_max, value=[edad_min, edad_max], allowCross=False), md=3),
    ], className="filter-box mb-4")


def graph_tabs():
    return dbc.Row([
        dcc.Tabs(id="tabs-graficos", value="tab-modalidad", children=[
            dcc.Tab(label="Modalidad", children=[dcc.Graph(id="grafico-modalidad")]),
            dcc.Tab(label="Especialidades", children=[dcc.Graph(id="grafico-especialidades")]),
            dcc.Tab(label="Género", children=[dcc.Graph(id="grafico-genero")]),
            dcc.Tab(label="Edad", children=[dcc.Graph(id="grafico-edad")]),
            dcc.Tab(label="Duración", children=[dcc.Graph(id="grafico-duracion")]),
        ])
    ], className="mb-4")


def mapa_component():
    return dbc.Row([
        dbc.Col(html.Iframe(id="mapa-consultas", srcDoc=generar_mapa_consultas(df_base), width="100%", height="600", style={"border": "none"}), md=12)
    ])


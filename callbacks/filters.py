from dash import Input, Output
import plotly.express as px
from utils.funciones import (
    cargar_datos,
    especialidades_top,
    modalidad_consultas
)
from maps.mapa_consultas import generar_mapa_consultas


def register_callbacks(app):
    @app.callback(
        Output("grafico-modalidad", "figure"),
        Output("grafico-especialidades", "figure"),
        Output("grafico-genero", "figure"),
        Output("grafico-edad", "figure"),
        Output("grafico-duracion", "figure"),
        Output("mapa-consultas", "srcDoc"),
        Input("dropdown-region", "value"),
        Input("dropdown-modalidad", "value"),
        Input("dropdown-especialidad", "value"),
        Input("dropdown-genero", "value"),
        Input("slider-edad", "value")
    )
    def actualizar_vistas(region, modalidad, especialidad, genero, rango_edad):
        df = cargar_datos()
        if region:
            df = df[df["region"] == region]
        if modalidad:
            df = df[df["tipo_consulta"] == modalidad]
        if especialidad:
            df = df[df["especialidad"] == especialidad]
        if genero:
            df = df[df["genero_paciente"] == genero]
        if rango_edad:
            df = df[(df["edad_paciente"] >= rango_edad[0]) & (df["edad_paciente"] <= rango_edad[1])]

        fig_modalidad = px.pie(
            modalidad_consultas(df),
            values=modalidad_consultas(df).values,
            names=modalidad_consultas(df).index,
            title="Distribución por modalidad"
        )

        top_especialidades = especialidades_top(df)
        fig_especialidades = px.bar(
            top_especialidades,
            x=top_especialidades.index,
            y=top_especialidades.values,
            labels={"x": "Especialidad", "y": "Cantidad"},
            title="Especialidades más consultadas"
        )

        genero_counts = df["genero_paciente"].value_counts()
        fig_genero = px.pie(
            genero_counts,
            values=genero_counts.values,
            names=genero_counts.index,
            title="Distribución por género"
        )

        fig_edad = px.histogram(
            df,
            x="edad_paciente",
            nbins=20,
            title="Distribución por edad"
        )

        fig_duracion = px.histogram(
            df,
            x="duracion_minutos",
            nbins=20,
            title="Duración de consultas"
        )

        mapa_html = generar_mapa_consultas(df)

        return (
            fig_modalidad,
            fig_especialidades,
            fig_genero,
            fig_edad,
            fig_duracion,
            mapa_html,
        )

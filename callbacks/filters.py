from dash import Input, Output
from utils.funciones import (
    cargar_datos,
    especialidades_top,
    modalidad_consultas
)
import plotly.express as px

# Callback para actualizar el gráfico de especialidades según modalidad
def register_callbacks(app):
    @app.callback(
        Output("grafico-especialidades", "figure"),
        Input("dropdown-modalidad", "value")
    )
    def actualizar_especialidades_por_modalidad(modalidad):
        df = cargar_datos()
        if modalidad:
            df = df[df["tipo_consulta"] == modalidad]

        top_especialidades = especialidades_top(df)

        fig = px.bar(
            top_especialidades,
            x=top_especialidades.index,
            y=top_especialidades.values,
            labels={"x": "Especialidad", "y": "Cantidad"},
            title=f"Especialidades más consultadas ({modalidad})"
        )
        return fig

    # Callback para actualizar gráfico de modalidad
    @app.callback(
        Output("grafico-modalidad", "figure"),
        Input("dropdown-region", "value")
    )
    def actualizar_modalidad_por_region(region):
        df = cargar_datos()
        if region:
            df = df[df["region"] == region]

        modalidades = modalidad_consultas(df)

        fig = px.pie(
            modalidades,
            values=modalidades.values,
            names=modalidades.index,
            title=f"Distribución por modalidad en {region}"
        )
        return fig

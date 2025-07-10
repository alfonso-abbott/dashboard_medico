import folium
from folium.plugins import MarkerCluster, HeatMap
from utils.funciones import cargar_datos


def color_por_especialidad(especialidad):
    colores = {
        "Cardiología": "red",
        "Pediatría": "green",
        "Dermatología": "orange",
        "Neurología": "purple",
        "Psiquiatría": "darkblue",
        "Oftalmología": "cadetblue",
        "Ginecología": "pink",
        "Traumatología": "gray",
    }
    return colores.get(especialidad, "blue")


def generar_mapa_consultas(df=None):
    if df is None:
        df = cargar_datos()
    df_mapa = df.head(500)

    mapa = folium.Map(
        location=[df_mapa["latitud"].mean(), df_mapa["longitud"].mean()],
        zoom_start=5,
        tiles="cartodb dark_matter",
    )

    heat_data = [[row["latitud"], row["longitud"]] for _, row in df_mapa.iterrows()]
    HeatMap(heat_data, radius=12, blur=15, min_opacity=0.4).add_to(mapa)

    marker_cluster = MarkerCluster().add_to(mapa)

    style = """
    <style>
    .popup-box{background-color:rgba(20,20,20,0.9);color:white;padding:8px;border-radius:5px;border:1px solid #00ffe1;}
    </style>
    """
    mapa.get_root().header.add_child(folium.Element(style))

    for _, fila in df_mapa.iterrows():
        popup_text = (
            f"<div class='popup-box'>"
            f"<b>Comuna:</b> {fila['comuna']}<br>"
            f"<b>Región:</b> {fila['region']}<br>"
            f"<b>Especialidad:</b> {fila['especialidad']}<br>"
            f"<b>Modalidad:</b> {fila['tipo_consulta']}<br>"
            f"<b>Edad:</b> {fila['edad_paciente']} años<br>"
            f"<b>Género:</b> {fila['genero_paciente']}"
            "</div>"
        )
        folium.Marker(
            location=[fila["latitud"], fila["longitud"]],
            popup=folium.Popup(popup_text, max_width=250),
            icon=folium.Icon(color=color_por_especialidad(fila["especialidad"]), icon="medkit", prefix="fa"),
        ).add_to(marker_cluster)

    return mapa._repr_html_()

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
        "Traumatología": "gray"
    }
    return colores.get(especialidad, "blue")

def generar_mapa_consultas():
    df = cargar_datos()
    df_mapa = df.head(500)  # Limitar para rendimiento

    mapa = folium.Map(
        location=[df_mapa["latitud"].mean(), df_mapa["longitud"].mean()],
        zoom_start=5,
        tiles="cartodb dark_matter"
    )

    # 🔥 Heatmap de densidad
    heat_data = [[row['latitud'], row['longitud']] for _, row in df_mapa.iterrows()]
    HeatMap(heat_data, radius=12, blur=15, min_opacity=0.4).add_to(mapa)

    # 📍 Clustering con íconos por especialidad
    marker_cluster = MarkerCluster().add_to(mapa)

    for _, fila in df_mapa.iterrows():
        popup_text = f"""
        <b>Ciudad:</b> {fila['ciudad']}<br>
        <b>Región:</b> {fila['region']}<br>
        <b>Especialidad:</b> {fila['especialidad']}<br>
        <b>Modalidad:</b> {fila['modalidad']}<br>
        <b>Edad:</b> {fila['edad']} años<br>
        <b>Género:</b> {fila['genero']}
        """
        folium.Marker(
            location=[fila["latitud"], fila["longitud"]],
            popup=popup_text,
            icon=folium.Icon(color=color_por_especialidad(fila["especialidad"]), icon="medkit", prefix="fa")
        ).add_to(marker_cluster)

    # 🔷 (Opcional) Cargar GeoJSON si se desea agregar polígonos regionales
    # from pathlib import Path
    # geojson_path = Path("maps/regiones_chile.geojson")
    # if geojson_path.exists():
    #     folium.GeoJson(
    #         data=geojson_path.read_text(encoding="utf-8-sig"),
    #         name="Regiones",
    #         style_function=lambda x: {
    #             "fillColor": "#228B22",
    #             "color": "green",
    #             "weight": 1,
    #             "fillOpacity": 0.2
    #         }
    #     ).add_to(mapa)

    # Exportar HTML para usar en Dash
    mapa.save("maps/mapa_output.html")
    return "maps/mapa_output.html"

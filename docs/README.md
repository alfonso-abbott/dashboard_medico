# 🧠 Dashboard Interactivo de Consultas Médicas en Chile 🇨🇱

Este proyecto consiste en un dashboard interactivo desarrollado con **Python**, **Dash**, **Plotly** y **Folium**. Permite visualizar datos simulados de 10.000 consultas médicas realizadas en Chile, ofreciendo estadísticas, mapas, KPIs y filtros personalizados.

---

## 📂 1. Estructura del Proyecto

```

/project-root
│
├── app.py
├── cards.py
├── filters.py
├── mapa\_consultas.py
├── funciones.py
├── generador\_dataset.py
├── data/
│   └── consultas\_medicas.csv
├── assets/
│   └── style.css
├── requirements.txt
└── README.md

```

---

## ⚙️ 2. Instalación

1. Clona el repositorio:

```bash
git clone https://github.com/usuario/dashboard-consultas.git
cd dashboard-consultas
```

2. Instala las dependencias:

```bash
pip install -r requirements.txt
```

3. Ejecuta la aplicación:

```bash
python app.py
```

---

## 📊 3. Funcionalidades

* KPIs segmentados por género, edad y duración de consultas
* Gráficos interactivos por especialidad y año
* Mapa georreferenciado con clustering (Folium)
* Filtros dinámicos por región, comuna y tipo de consulta
* Interfaz moderna con estilo oscuro (neón) ✨

---

## 🧬 4. Dataset

El dataset fue generado de forma sintética con la librería `Faker`. Contiene **10.000 registros simulados** de consultas médicas en Chile (2022-2024). Se encuentra en:

```
/data/consultas_medicas.csv
```

---

## 📍 5. Mapa Interactivo

La visualización georreferenciada se genera con `Folium`, utilizando:

* Agrupación con `MarkerCluster`
* Íconos personalizados
* Popup con datos detallados
* Exportación a `HTML` para incrustarse en Dash

---

## 🖼️ 6. Capturas

*Agrega aquí imágenes del dashboard, KPIs y mapa.*

---

## 📋 7. Dependencias

```txt
pandas==2.2.2
numpy==1.26.4
faker==24.9.0
dash==2.16.1
plotly==5.21.0
folium==0.16.0
```

Puedes generar este archivo automáticamente con:

```bash
pip freeze > requirements.txt
```

---

## 💻 8. Ejecución Local

Lanza la app en tu PC con:

```bash
python app.py
```

Por defecto, estará en:
[http://127.0.0.1:8050](http://127.0.0.1:8050)

---

## 🚀 9. Despliegue Online con Render

1. Sube tu proyecto a GitHub
2. Crea cuenta en [Render](https://render.com)
3. Configura el servicio con:

| Parámetro    | Valor                               |
| ------------- | ----------------------------------- |
| Runtime       | Python 3.x                          |
| Build Command | `pip install -r requirements.txt` |
| Start Command | `python app.py`                   |

4. Asegúrate de tener en `app.py`:

```python
if __name__ == '__main__':
    app.run_server(debug=False, host='0.0.0.0', port=10000)
```

5. ¡Listo! Agrega aquí tu demo online 👇

🔗 DEMO: [https://dashboard-consultas.onrender.com](https://dashboard-consultas.onrender.com)

---

## 👨‍💻 Autor

**Alfonso**
Proyecto técnico de dashboards interactivos con Python (Dash + Plotly + Folium).
Santiago, Chile.

```

---
```

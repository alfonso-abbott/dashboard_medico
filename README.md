# Futuristic Medical Consultations Dashboard

This project is an interactive dashboard built with **Dash**, **Plotly** and **Folium** to explore 10,000 simulated medical consultations in Chile. The interface uses a modern cyborg style with neon accents and provides dynamic filters, KPIs and a map.

## Screenshots

*Add here some screenshots of the dashboard and the map.*

## Running locally

```bash
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python app.py
```

Then open `http://localhost:8050` in your browser.

## Deploying on Render

1. Push this repository to GitHub.
2. Create a new **Web Service** on [Render](https://render.com).
3. Set the build command to `pip install -r requirements.txt` and the start command to `gunicorn app:server`.
4. Make sure `Procfile` is present with:
   ```
   web: gunicorn app:server
   ```
5. The service will be accessible at the URL provided by Render.

## Technologies

- Dash & Dash Bootstrap Components
- Plotly
- Folium
- Pandas / NumPy
- Gunicorn

## Credits

Data generated with `Faker`. Dashboard created for demonstration purposes.


import pandas as pd
import numpy as np
import random
from faker import Faker
import os

fake = Faker('es_CL')

# Parámetros
N = 10000  # cantidad de registros

especialidades = ['Cardiología', 'Pediatría', 'Dermatología', 'Neurología',
                  'Psiquiatría', 'Oftalmología', 'Ginecología', 'Traumatología']
regiones_comunas = {
    'Región Metropolitana': ['Santiago', 'Puente Alto', 'Maipú', 'La Florida'],
    'Valparaíso': ['Valparaíso', 'Viña del Mar', 'Quilpué'],
    'Biobío': ['Concepción', 'Talcahuano', 'Los Ángeles'],
    'Araucanía': ['Temuco', 'Padre Las Casas'],
    'Antofagasta': ['Antofagasta', 'Calama'],
    'Los Lagos': ['Puerto Montt', 'Osorno']
}
tipos = ['Presencial', 'Online']
generos = ['Masculino', 'Femenino', 'Otro']

def generar_lat_lon(region, comuna):
    # Valores de ejemplo por comuna (simulados)
    coordenadas = {
        'Santiago': (-33.45, -70.66),
        'Concepción': (-36.82, -73.05),
        'Valparaíso': (-33.04, -71.62),
        'Puerto Montt': (-41.47, -72.94),
        'Antofagasta': (-23.65, -70.40),
        'Temuco': (-38.73, -72.59)
    }
    base = coordenadas.get(comuna, (-33.45, -70.66))
    lat = base[0] + random.uniform(-0.01, 0.01)
    lon = base[1] + random.uniform(-0.01, 0.01)
    return round(lat, 6), round(lon, 6)

datos = []

for i in range(N):
    region = random.choice(list(regiones_comunas.keys()))
    comuna = random.choice(regiones_comunas[region])
    lat, lon = generar_lat_lon(region, comuna)

    datos.append({
        'id_consulta': i + 1,
        'fecha': fake.date_between(start_date='-2y', end_date='today'),
        'especialidad': random.choice(especialidades),
        'region': region,
        'comuna': comuna,
        'tipo_consulta': random.choice(tipos),
        'genero_paciente': random.choice(generos),
        'edad_paciente': random.randint(0, 95),
        'duracion_minutos': round(np.random.normal(30, 10), 1),
        'resolutiva': random.choice(['Sí', 'No']),
        'latitud': lat,
        'longitud': lon
    })

df = pd.DataFrame(datos)

# Guardar archivo
ruta = 'data/consultas_medicas.csv'
os.makedirs('data', exist_ok=True)
df.to_csv(ruta, index=False, encoding='utf-8-sig')

print(f"✅ Dataset generado exitosamente con {N} filas y guardado en {ruta}")

import pandas as pd
from pathlib import Path

# Cargar datos desde CSV (se reutiliza en múltiples partes del dashboard)
def cargar_datos():
    path = Path("data/dataset_limpio.csv")
    if not path.exists():
        path = Path("data/consultas_medicas.csv")
    return pd.read_csv(path)

# Total de consultas realizadas
def total_consultas(df):
    return len(df)

# Especialidades más frecuentes
def especialidades_top(df, n=5):
    return df['especialidad'].value_counts().head(n)

# Consultas por región
def consultas_por_region(df):
    return df['region'].value_counts()

# Promedio de duración de las consultas
def duracion_promedio(df):
    return round(df['duracion_minutos'].mean(), 1)

# Total por modalidad (presencial vs online)
def modalidad_consultas(df):
    return df['tipo_consulta'].value_counts()

def listar_regiones(df):
    return sorted(df['region'].unique())


def listar_especialidades(df):
    return sorted(df['especialidad'].unique())


def listar_modalidades(df):
    return sorted(df['tipo_consulta'].unique())


def listar_generos(df):
    return sorted(df['genero_paciente'].unique())


def rango_edad(df):
    return int(df['edad_paciente'].min()), int(df['edad_paciente'].max())


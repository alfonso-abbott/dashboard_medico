import pandas as pd

# Cargar datos desde CSV (se reutiliza en múltiples partes del dashboard)
def cargar_datos():
    return pd.read_csv("data/consultas_medicas.csv")

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
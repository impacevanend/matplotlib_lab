import pandas as pd
import plotly.graph_objects as go
import plotly.express as px

# Dataset 
data = {
    'id': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],
    'materia': ['Matemáticas', 'Historia', 'Ciencias', 'Lenguaje', 'Matemáticas',
                'Historia', 'Ciencias', 'Lenguaje', 'Matemáticas', 'Historia',
                'Ciencias', 'Lenguaje', 'Matemáticas', 'Historia', 'Ciencias',
                'Lenguaje', 'Matemáticas', 'Historia', 'Ciencias', 'Lenguaje'],
    'nota': [80, 65, 90, 75, 95, 70, 85, 60, 78, 82, 93, 68, 73, 88, 77, 50, 92, 63, 85, 79],
    'aprobado': ['Sí', 'No', 'Sí', 'Sí', 'Sí', 'Sí', 'Sí', 'No', 'Sí', 'Sí',
                 'Sí', 'Sí', 'Sí', 'Sí', 'Sí', 'No', 'Sí', 'No', 'Sí', 'Sí']
}

# DataFrame 
df = pd.DataFrame(data)

# Graficar con boxplot 
fig_boxplot = px.box(df, x='materia', y='nota', color='materia', title='Distribución de Notas')
fig_boxplot.show()

# pie chart
aprobados_count = df['aprobado'].value_counts().reset_index()
aprobados_count.columns = ['aprobado', 'count']

# Graficar con  Plotly Express
fig_pie = px.pie(aprobados_count, values='count', names='aprobado', title='Distribución de Aprobados')
fig_pie.show()
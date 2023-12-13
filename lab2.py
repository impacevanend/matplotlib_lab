import pandas as pd
import matplotlib.pyplot as plt

# dataset
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

# Función boxplot
def graficar_boxplot(df):
    
    materias = ['Matemáticas', 'Historia', 'Ciencias', 'Lenguaje']
    notas = [df[df['materia'] == materia]['nota'] for materia in materias]

    plt.figure(figsize=(10, 8))
    plt.boxplot(notas, labels=materias)
    plt.title('Distribución de Notas')
    plt.ylabel('Nota')
    plt.grid(True)
    plt.show()

# Función chart
def graficar_pie_chart(df):
    
    aprobados = df['aprobado'].value_counts()

    plt.figure(figsize=(6, 6))
    plt.pie(aprobados, labels=aprobados.index, autopct='%1.1f%%', startangle=90, colors=['blue', 'red'])
    plt.title('Distribución de Aprobados')
    plt.show()

# Llamar a las funciones de gráficos
graficar_boxplot(df)
graficar_pie_chart(df)
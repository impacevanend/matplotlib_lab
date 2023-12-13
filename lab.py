import matplotlib.pyplot as plt
import numpy as np

# Generar datos sintéticos según el script proporcionado
rng = np.random.default_rng(42)

# Datos de calificaciones de los estudiantes
matematicas = rng.integers(50, 100, 20)
ciencias = rng.integers(40, 95, 20)
literatura = rng.integers(60, 100, 20)

# Datos de errores para el gráfico de barras de error
errores_matematicas = rng.uniform(2, 5, 2)
errores_matematicas = [min(errores_matematicas), max(errores_matematicas)]

errores_ciencias = rng.uniform(1, 4, 2)
errores_ciencias = [min(errores_ciencias), max(errores_ciencias)]

errores_literatura = rng.uniform(3, 6, 2)
errores_literatura = [min(errores_literatura), max(errores_literatura)]

# Función para crear un gráfico de dispersión
def crear_grafico_dispersion(x, y, x_label, y_label, title):
    plt.figure(figsize=(8, 6))
    plt.scatter(x, y)
    plt.title(title)
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.grid(True)
    plt.show()

# Función para crear un gráfico de barras de error
def crear_grafico_barras_error(materias, calificaciones, errores, x_label, y_label, title, leyenda):
    plt.figure(figsize=(8, 6))
    plt.errorbar(materias, calificaciones, yerr=errores, fmt='o', ecolor='blue', capsize=5, label=leyenda)
    plt.title(title)
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.legend()
    plt.grid(True)
    plt.show()

# Función para crear un histograma
def crear_histograma(datos, x_label, y_label, title):
    plt.figure(figsize=(8, 6))
    plt.hist(datos, bins=range(50, 105, 5), color='blue', edgecolor='black')
    plt.title(title)
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.grid(True)
    plt.show()

# Gráfico de dispersión
crear_grafico_dispersion(
    x=matematicas,
    y=ciencias,
    x_label='Calificaciones de Matemáticas',
    y_label='Calificaciones de Ciencias',
    title='Relación entre las calificaciones de Matemáticas y Ciencias'
)

# Gráfico de barras de error
promedios = [np.mean(matematicas), np.mean(ciencias), np.mean(literatura)]
errores = [np.mean(errores_matematicas), np.mean(errores_ciencias), np.mean(errores_literatura)]
materias = ['Matemáticas', 'Ciencias', 'Literatura']

crear_grafico_barras_error(
    materias=materias,
    calificaciones=promedios,
    errores=errores,
    x_label='Materias',
    y_label='Calificaciones promedio',
    title='Calificaciones promedio con barras de error',
    leyenda='Promedio'
)

# Histograma
crear_histograma(
    datos=matematicas,
    x_label='Calificaciones de Matemáticas',
    y_label='Frecuencia',
    title='Distribución de las calificaciones de Matemáticas'
)

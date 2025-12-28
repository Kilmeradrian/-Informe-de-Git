from functools import reduce
# Datos inmutables
estudiantes = ("Kilmer", "Sadalla", "Adrián", "Alexandra", "Adripan", "Pablo", "Lucía")
notas = (8.5, 6.9, 9.2, 7.8, 5.4, 6.0, 9.6)
# Funciones puras
def aprobar(nota):
    return nota >= 7
def clasificar(nota):
    return (
        "Excelente" if nota >= 9 else
        "Bueno" if nota >= 8 else
        "Regular" if nota >= 7 else
        "Deficiente"
    )
def diferencia_promedio(promedio):
    return lambda nota: abs(nota - promedio)
# Análisis funcional
# Promedio general
promedio = reduce(lambda acc, n: acc + n, notas) / len(notas)
# Relación estudiante - nota
registro = tuple(zip(estudiantes, notas))
# Aprobados y reprobados
aprobados = tuple(filter(lambda x: aprobar(x[1]), registro))
reprobados = tuple(filter(lambda x: not aprobar(x[1]), registro))
# Porcentajes
porcentaje = lambda grupo: round(len(grupo) * 100 / len(registro), 2)
porcentaje_aprobados = porcentaje(aprobados)
porcentaje_reprobados = porcentaje(reprobados)

# Clasificación académica
clasificacion = tuple(
    map(lambda x: (x[0], x[1], clasificar(x[1])), registro)
)
# Conteo por categoría
contar_categoria = lambda categoria: len(
    tuple(filter(lambda x: x[2] == categoria, clasificacion))
)
resumen_categorias = {
    "Excelente": contar_categoria("Excelente"),
    "Bueno": contar_categoria("Bueno"),
    "Regular": contar_categoria("Regular"),
    "Deficiente": contar_categoria("Deficiente")
}
# Desviación promedio
desviacion_promedio = reduce(
    lambda acc, n: acc + diferencia_promedio(promedio)(n),
    notas,
    0
) / len(notas)
# Estado del curso
estado_curso = (
    "Curso aprobado"
    if porcentaje_aprobados >= 70
    else "Curso en riesgo académico"
)

print("=== Análisis Académico Final ===\n")
print("Promedio general:", round(promedio, 2))
print("Desviación promedio:", round(desviacion_promedio, 2))
print("\nPorcentaje de aprobados:", porcentaje_aprobados, "%")
print("Porcentaje de reprobados:", porcentaje_reprobados, "%")
print("Estado del curso:", estado_curso)
print("\nClasificación académica:")
print(clasificacion)
print("\nResumen por categoría:")
print(resumen_categorias)

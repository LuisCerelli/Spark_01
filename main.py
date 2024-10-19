from pyspark.sql import SparkSession
from pyspark.sql.functions import col

# 1. Crear una sesión de Spark
spark = SparkSession.builder \
    .appName("Spark Ingeniería de Datos") \
    .getOrCreate()

# 2. Crear un DataFrame a partir de una lista de datos
data = [
    ("Luis", "Delprado", 34, "Argentina"),
    ("Juan", "Perez", 28, "España"),
    ("Maria", "Gomez", 42, "Francia"),
    ("Ana", "Martinez", 35, "Italia"),
]

# Especificar nombres de columnas
columns = ["Nombre", "Apellido", "Edad", "País"]

# Crear DataFrame
df = spark.createDataFrame(data, columns)

# 3. Mostrar el DataFrame
print("DataFrame original:")
df.show()

# 4. Filtrar los datos (ejemplo: personas mayores de 30 años)
print("Filtrar personas mayores de 30 años:")
df.filter(col("Edad") > 30).show()

# 5. Seleccionar columnas específicas
print("Seleccionar columnas Nombre y Edad:")
df.select("Nombre", "Edad").show()

# 6. Añadir una nueva columna (ejemplo: Categorizar la edad)
print("Añadir columna 'Categoría Edad':")
df = df.withColumn("Categoría Edad", 
                   col("Edad").cast("int") > 30)  # True si mayor de 30, False si no
df.show()

# 7. Agrupar datos (ejemplo: contar cuántas personas por país)
print("Agrupar y contar por país:")
df.groupBy("País").count().show()

# 8. Ordenar datos (ejemplo: por edad de mayor a menor)
print("Ordenar por edad descendente:")
df.orderBy(col("Edad").desc()).show()

# 9. Parar la sesión de Spark
spark.stop()

# Proyecto: Ejemplo de Uso de PySpark en Ingeniería de Datos

## Descripción

Este proyecto demuestra cómo utilizar **PySpark**, la interfaz de Apache Spark para Python, en el contexto de ingeniería de datos. El código muestra cómo crear un **DataFrame** en Spark a partir de una lista de datos y realizar operaciones básicas de manipulación y transformación. PySpark permite el manejo de grandes volúmenes de datos de manera distribuida, y es ideal para entornos en los que se necesita escalabilidad y eficiencia en el procesamiento de datos.

## Funcionalidades

El script realiza las siguientes acciones:

1. **Creación de una sesión de Spark**: Se inicializa una sesión de Spark, que es el punto de entrada para cualquier operación con datos utilizando PySpark.
   
2. **Creación de un DataFrame**: A partir de una lista de datos, se genera un DataFrame con columnas predefinidas (Nombre, Apellido, Edad, País).
   
3. **Mostrar los datos**: Se muestra el contenido completo del DataFrame original en formato tabular.
   
4. **Filtrar datos**: Se aplican filtros para seleccionar solo las personas mayores de 30 años.

5. **Seleccionar columnas**: Se seleccionan únicamente las columnas de interés (Nombre y Edad) del DataFrame original.

6. **Añadir una columna**: Se añade una columna nueva que categoriza las edades, indicando si la persona tiene más de 30 años (True o False).

7. **Agrupar datos**: Se agrupan las personas por país y se realiza un conteo de cuántas personas corresponden a cada país.

8. **Ordenar datos**: Se ordenan los registros por edad de mayor a menor, lo que facilita la visualización de las personas más mayores primero.

9. **Parar la sesión de Spark**: Finaliza la sesión de Spark una vez completadas las operaciones, liberando los recursos utilizados.

## Ejemplo de uso

Este código puede utilizarse en un entorno de análisis de datos cuando se tiene información en formato tabular y se desean aplicar diversas transformaciones y análisis de manera eficiente. Por ejemplo, en un entorno de recursos humanos donde se quiera analizar la edad de empleados de diferentes países, filtrar aquellos que cumplan ciertos criterios (como la edad), y generar informes agregados por nacionalidad.

Para ejecutar el código, asegúrate de haber instalado PySpark con el siguiente comando:

```bash
pip install pyspark
```

Luego, simplemente ejecuta el script en tu entorno de desarrollo de Python. Spark manejará la creación de sesiones y la distribución de datos, incluso si trabajas con grandes volúmenes de información.

## Consideraciones

- **Escalabilidad**: PySpark es ideal cuando el volumen de datos supera la capacidad de la memoria local. Si tu conjunto de datos es pequeño, Pandas puede ser más rápido y sencillo.
- **Entorno distribuido**: El código puede ejecutarse tanto en un entorno local como en un clúster de Spark, permitiendo el procesamiento distribuido de los datos.
- **Persistencia de datos**: Si los datos no están disponibles localmente, puedes integrarlos desde sistemas distribuidos como HDFS o bases de datos conectadas a Spark.

---

## **Utilidad en Ingeniería de Datos**

**Este código es especialmente útil en proyectos de Ingeniería de Datos** porque permite aplicar transformaciones y análisis de datos distribuidos de manera eficiente. En un entorno donde los datos suelen provenir de múltiples fuentes y formatos, PySpark facilita la integración y procesamiento a gran escala. Además, la capacidad de Spark para trabajar con clústeres y su procesamiento paralelo lo convierten en una herramienta poderosa para manejar Big Data en tiempo real, realizar ETL (Extract, Transform, Load) y crear pipelines de datos robustos.

Con PySpark, puedes construir flujos de trabajo que no solo procesan grandes volúmenes de datos, sino que también los transforman en información valiosa para la toma de decisiones estratégicas.


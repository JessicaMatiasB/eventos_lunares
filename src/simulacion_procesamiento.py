from pyspark.sql import SparkSession
from pyspark.sql.functions import udf, col, year
from pyspark.sql.types import StringType, TimestampType
import random
from faker import Faker
from datetime import datetime, timedelta
import os

# Inicializar Faker y crear una sesión de Spark
fake = Faker()
spark = SparkSession.builder.appName("Prueba tecnica").config("spark.sql.shuffle.partitions", "4").getOrCreate()

# Definir el número de filas a generar
num_filas = 10**7

# Funciónes UDF para generar el datset fake
# Función UDF para generar UUID
@udf(StringType())
def uuid_generator():
    return str(fake.uuid4())

# Función UDF para generar el tipo de evento
@udf(StringType())
def typeEvent_generator():
    list_eventos = ["lunar", "solar", "asteroid", "lluvia de estrellas", "cometas", "meteoros"]
    return random.choice(list_eventos)

# Función UDF para generar timestamps aleatorios
@udf(TimestampType())
def random_timestamp_generator():
    start = datetime(2013, 1, 1)
    end = datetime(2025, 12, 31)
    delta = end - start
    random_seg = random.randint(0, int(delta.total_seconds()))
    return start + timedelta(seconds=random_seg)

# Función UDF para generar ubicaciones
@udf(StringType())
def location_genrator():
    return fake.city()

# Función UDF para generar descriociones
@udf(StringType())
def details_generator():
    return fake.sentence(20)

# Crear un DataFrame vacío
df = spark.range(0, num_filas).toDF("id")

# Añadir columnas con datos generados
df = df.withColumn("id_evento", uuid_generator())
df = df.withColumn("tipo_evento", typeEvent_generator())
df = df.withColumn("timestamp", random_timestamp_generator())
df = df.withColumn("ubicacion", location_genrator())
df = df.withColumn("detalles", details_generator())

# Definir rutas relativas para guardar los archivos
directorio_actual = os.path.dirname(__file__)
carpeta_data = os.path.join(directorio_actual, "data")
path = os.path.join(directorio_actual, "data")
path_output = os.path.join(directorio_actual, "datamart")

# Vericar de que la carpeta 'data' y 'datamart' existe
os.makedirs(carpeta_data, exist_ok=True)
os.makedirs(carpeta_data, exist_ok=True)

df.write.mode("overwrite").parquet(path)

import findspark
import pyspark
print("¡PySpark se importó correctamente!")
from pyspark.sql import SparkSession

findspark.init()
spark = SparkSession.builder.getOrCreate
spark
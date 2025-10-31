import findspark
findspark.init()

from pyspark.sql import SparkSession

spark = SparkSession.builder \
    .appName("Test Spark 3.2") \
    .getOrCreate()

print("Versión de Spark:", spark.version)
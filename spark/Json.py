from pyspark.sql import SparkSession

spark = SparkSession.builder.appName('pyspark').config('key','value').getOrCreate()


df=spark.read.json("examples/src/main/resources/people.json")
df.show()

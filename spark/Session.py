from pyspark.sql import SparkSession

spark=SparkSession.builder.appName('pyspark app').config('key','value').getOrCreate
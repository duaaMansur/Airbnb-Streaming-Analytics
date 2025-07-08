from pyspark.sql import SparkSession

# Initialize a SparkSession
spark = (
    SparkSession.builder
    .appName("TestSparkApp")
    .config("spark.driver.memory", "4g")
    .getOrCreate()
)

# Check SparkSession status
print("SparkSession successfully created!")
spark.stop()


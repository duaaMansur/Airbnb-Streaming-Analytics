from pyspark.sql import SparkSession
from pyspark.sql.functions import expr

# Initialize SparkSession
spark = SparkSession.builder \
    .appName("KafkaSparkStream") \
    .getOrCreate()

# Read streaming data from Kafka topic
kafka_df = spark.readStream \
    .format("kafka") \
    .option("kafka.bootstrap.servers", "localhost:9092") \
    .option("subscribe", "airbnb-events") \
    .load()

# The Kafka data is in binary format, so decode it
kafka_df = kafka_df.selectExpr("CAST(key AS STRING)", "CAST(value AS STRING)")

# Process the streaming data (Example: Displaying the data)
query = kafka_df.writeStream \
    .outputMode("append") \
    .format("console") \
    .start()

query.awaitTermination()
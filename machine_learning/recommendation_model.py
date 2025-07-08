from pyspark.sql import SparkSession
from pyspark.ml.recommendation import ALS
from pyspark.sql.functions import col, when
from cassandra.cluster import Cluster

spark = (
    SparkSession.builder.appName("AirbnbRecommendationModel")
    .config("spark.cassandra.connection.host", "127.0.0.1")
    .config("spark.cassandra.connection.port", "9042")  # Default Cassandra port
    .getOrCreate()
)

# Connect to Cassandra
cluster = Cluster(['127.0.0.1'])
session = cluster.connect('airbnb')

# Load data from Cassandra
df = spark.read \
    .format("org.apache.spark.sql.cassandra") \
    .options(table="bookings", keyspace="airbnb") \
    .load()

# Map 'action' column to numeric values for ALS
df = df.withColumn("action", when(col("action") == "booked", 5)
                   .when(col("action") == "viewed", 3)
                   .when(col("action") == "canceled", 1)
                   .otherwise(0))

# Train the ALS model
als = ALS(userCol="user_id", itemCol="listing_id", ratingCol="action", coldStartStrategy="drop")
model = als.fit(df)

# Make recommendations for all users
user_recommendations = model.recommendForAllUsers(10)

# Show the top 10 recommendations for each user
user_recommendations.show(truncate=False)

# Save the model
model.save("/home/rabail/airbnb-bigdata/airbnb-bigdata/model")
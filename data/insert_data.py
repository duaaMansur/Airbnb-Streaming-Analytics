from cassandra.cluster import Cluster
import random
import time
from datetime import datetime

# Connect to Cassandra
cluster = Cluster(['127.0.0.1'])
session = cluster.connect('airbnb')

# Insert 1000 rows into the bookings table
for i in range(1, 1001):
    user_id = i
    unix_timestamp = time.time() + random.randint(1, 1000)  # Current timestamp + random offset
    timestamp = datetime.fromtimestamp(unix_timestamp)  # Convert to a datetime object
    action = random.choice(['booked', 'viewed', 'canceled'])
    listing_id = random.randint(100, 500)
    price = round(random.uniform(50, 500), 2)  # Price per night in USD
    location = random.choice(['New York', 'Los Angeles', 'San Francisco', 'Chicago', 'Miami'])
    room_type = random.choice(['Entire home/apt', 'Private room', 'Shared room'])
    guests = random.randint(1, 6)  # Number of guests
    nights = random.randint(1, 14)  # Number of nights booked
    host_id = random.randint(1, 300)  # Host ID for the listing
    cancellation_policy = random.choice(['flexible', 'moderate', 'strict'])

    query = """
    INSERT INTO bookings (user_id, timestamp, action, listing_id, price, location, room_type, guests, nights, host_id, cancellation_policy)
    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
    """
    session.execute(query, (user_id, timestamp, action, listing_id, price, location, room_type, guests, nights, host_id, cancellation_policy))
    print(f"Inserted row {i} - user_id: {user_id}, action: {action}, listing_id: {listing_id}, price: {price}, location: {location}")

print("1000 rows inserted successfully.")

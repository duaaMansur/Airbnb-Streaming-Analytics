from confluent_kafka import Producer
import json
import time
import random

# Create a Kafka producer
producer = Producer({'bootstrap.servers': 'localhost:9092'})

def send_event():
    user_id = 1  # Start user ID at 1
    actions = ["booked", "viewed", "canceled"]  # Possible user actions

    while True:  # Run indefinitely until manually stopped
        event = {
            "user_id": user_id,
            "listing_id": random.randint(100, 500),  # Random listing ID between 100 and 500
            "action": random.choice(actions),  # Random action from the list
            "timestamp": time.time()  # Current timestamp
        }
        producer.produce('airbnb-events', value=json.dumps(event))
        print(f"Sent event: {event}")
        user_id += 1  # Increment user_id
        time.sleep(0.01)  # Slight delay to simulate real-time events

    # Wait for any outstanding messages to be delivered
    producer.flush()

if __name__ == "__main__":
    send_event()

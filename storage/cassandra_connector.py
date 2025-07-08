from cassandra.cluster import Cluster

def create_keyspace():
    cluster = Cluster(['127.0.0.1'])
    session = cluster.connect()
    session.execute("""
    CREATE KEYSPACE IF NOT EXISTS airbnb
    WITH replication = {'class': 'SimpleStrategy', 'replication_factor': '1'}
    """)
    session.set_keyspace('airbnb')
    session.execute("""
    CREATE TABLE IF NOT EXISTS bookings (
        user_id INT,
        listing_id INT,
        action TEXT,
        timestamp DOUBLE,
        PRIMARY KEY (user_id, timestamp)
    )
    """)
    print("Keyspace and table created.")

if __name__ == "__main__":
    create_keyspace()


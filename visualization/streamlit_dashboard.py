import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from cassandra.cluster import Cluster
from cassandra.query import dict_factory
from datetime import datetime

# Streamlit app title and description
st.title("Airbnb Booking Actions Dashboard")
st.markdown("""
Welcome to the Airbnb Dashboard! This dashboard provides insights into bookings, cancellations, and user actions on Airbnb listings.
""")

# Function to connect to Cassandra and fetch live data
def fetch_live_data():
    cluster = Cluster(['127.0.0.1'])  # Replace with your Cassandra cluster IP
    session = cluster.connect()
    session.set_keyspace('airbnb')
    session.row_factory = dict_factory  # Return rows as dictionaries

    query = "SELECT * FROM bookings"
    rows = session.execute(query)

    # Convert rows to a pandas DataFrame
    data = pd.DataFrame(list(rows))
    data["timestamp"] = pd.to_datetime(data["unix_timestamp"], unit="s")  # Convert UNIX timestamp to datetime
    return data

# Streamlit App Title
st.title("📊 Real-Time Airbnb Booking Dashboard")

# Sidebar Filters
st.sidebar.header("🔧 Filters")
selected_action = st.sidebar.multiselect(
    "Select Actions",
    options=['booked', 'viewed', 'canceled'],
    default=['booked', 'viewed', 'canceled']
)

# Fetch live data from Cassandra
try:
    live_data = fetch_live_data()
    filtered_data = live_data[live_data["action"].isin(selected_action)]
except Exception as e:
    st.error(f"Error fetching data: {e}")
    filtered_data = pd.DataFrame()  # Empty DataFrame in case of error

# Raw Data Display
st.subheader("Filtered Data")
st.write(filtered_data)

# Visualizations
st.subheader("📈 Visualizations")

# Action Count Bar Chart
st.markdown("### Action Counts")
if not filtered_data.empty:
    action_counts = filtered_data["action"].value_counts()
    st.bar_chart(action_counts)
else:
    st.info("No data available for the selected filters.")

# Top Listings by Actions
st.markdown("### Top Listings by Actions")
if not filtered_data.empty:
    top_listings = (
        filtered_data.groupby("listing_id")
        .size()
        .reset_index(name="action_count")
        .sort_values(by="action_count", ascending=False)
        .head(10)
    )
    st.write(top_listings)


# Action Distribution by Listing
st.markdown("### Action Distribution by Listing")
if not filtered_data.empty:
    fig, ax = plt.subplots(figsize=(12, 6))
    sns.countplot(data=filtered_data, x="listing_id", hue="action", palette="viridis", ax=ax)
    ax.set_title("Action Distribution by Listing")
    ax.set_xlabel("Listing ID")
    ax.set_ylabel("Count")
    ax.tick_params(axis="x", rotation=90)
    st.pyplot(fig)



import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Sample data for Airbnb bookings
data = {
    "user_id": [769, 23, 114, 660, 893, 53, 987, 878, 110, 91],
    "timestamp": [
        "2025-01-26 23:23:21", "2025-01-26 23:12:08", "2025-01-26 23:25:56",
        "2025-01-26 23:20:30", "2025-01-26 23:26:23", "2025-01-26 23:12:14",
        "2025-01-26 23:12:19", "2025-01-26 23:14:03", "2025-01-26 23:18:57",
        "2025-01-26 23:16:47"
    ],
    "action": ["booked", "canceled", "canceled", "booked", "canceled", "canceled", "viewed", "canceled", "viewed", "canceled"],
    "cancellation_policy": ["strict", "flexible", "moderate", "flexible", "strict", "flexible", "flexible", "moderate", "strict", "strict"],
    "guests": [4, 5, 4, 1, 4, 4, 2, 1, 3, 4],
    "host_id": [6, 74, 13, 214, 62, 125, 47, 260, 110, 14],
    "listing_id": [229, 382, 109, 236, 368, 377, 303, 357, 408, 143],
    "location": ["Miami", "New York", "Chicago", "New York", "Chicago", "Chicago", "Chicago", "San Francisco", "San Francisco", "San Francisco"],
    "nights": [1, 5, 8, 8, 14, 1, 13, 1, 2, 10],
    "price": [360.44, 194.55, 96.75, 481.06, 121.43, 469.93, 414.65, 471.9, 416.33, 301.73],
    "room_type": ["Private room", "Shared room", "Shared room", "Entire home/apt", "Shared room", "Entire home/apt", "Shared room", "Shared room", "Entire home/apt", "Shared room"]
}

# Create a DataFrame
df = pd.DataFrame(data)

# Convert timestamp to datetime format
df["timestamp"] = pd.to_datetime(df["timestamp"])

# Streamlit app title and description
st.title("Airbnb Booking Actions Dashboard")
st.markdown("""
Welcome to the Airbnb Dashboard! This dashboard provides insights into bookings, cancellations, and user actions on Airbnb listings.
""")

# Sidebar Filters
st.sidebar.header("Filters")
selected_action = st.sidebar.multiselect(
    "Select Actions",
    options=df["action"].unique(),
    default=df["action"].unique()
)
selected_location = st.sidebar.multiselect(
    "Select Locations",
    options=df["location"].unique(),
    default=df["location"].unique()
)

# Filter Data
filtered_data = df[(df["action"].isin(selected_action)) & (df["location"].isin(selected_location))]

# Display Raw Data
st.subheader("Filtered Data")
st.write(filtered_data)

# Visualizations

# Action Count Bar Chart
st.subheader("Action Counts")
action_counts = filtered_data["action"].value_counts()
st.bar_chart(action_counts)

# Average Price by Room Type
st.subheader("Average Price by Room Type")
avg_price_by_room = filtered_data.groupby("room_type")["price"].mean()
st.bar_chart(avg_price_by_room)

# Distribution of Room Types by Actions
st.subheader("Room Type Distribution by Actions")
fig, ax = plt.subplots(figsize=(10, 6))
sns.countplot(data=filtered_data, x="room_type", hue="action", palette="viridis", ax=ax)
ax.set_title("Room Type Distribution by Actions")
ax.set_xlabel("Room Type")
ax.set_ylabel("Count")
st.pyplot(fig)

# Top Hosts by Bookings
st.subheader("Top Hosts by Bookings")
top_hosts = (
    filtered_data[filtered_data["action"] == "booked"]
    .groupby("host_id")
    .size()
    .reset_index(name="booking_count")
    .sort_values(by="booking_count", ascending=False)
    .head(10)
)
st.write(top_hosts)

# Footer
st.markdown("---")
st.markdown("*Powered by Airbnb booking data!*")

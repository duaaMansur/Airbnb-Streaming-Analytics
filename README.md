# Airbnb Real-Time Big Data Analytics

> Real-time analytics pipeline for Airbnb user interactions using Kafka, Spark Streaming, Cassandra, and Streamlit.

## Project Overview

This project demonstrates a real-time big data solution for analyzing Airbnb user activities such as bookings, cancellations, and views. It provides live visual insights to support better decision-making on the platform.

---

## Tech Stack

- **Apache Kafka** – Real-time event ingestion  
- **Apache Spark Streaming** – Stream processing and transformation  
- **Apache Cassandra** – Scalable NoSQL data storage  
- **Streamlit** – Interactive dashboard for visual insights  
- **Docker Compose** – Container orchestration  
- **Python** – Data pipeline and dashboard scripts

---

## Architecture

```

Kafka → Spark Streaming → Cassandra → Streamlit

````

---

## 📁 Project Structure

```text
.
├── docker-compose.yml          # Container orchestration for Kafka, Spark, Cassandra
├── requirements.txt            # Python dependencies
├── streamlit.py                # Streamlit dashboard script
├── test_spark.py               # Spark test or example script
│
├── data/                       # Sample input data (if applicable)
├── env/                        # Virtual environment or environment configs
├── ingestion/                  # Kafka producers or data ingestion scripts
├── machine_learning/           # ML scripts for prediction (future work)
├── processing/                 # Spark data processing jobs
├── storage/                    # Cassandra DB setup/schema or scripts
├── visualization/              # Dashboard and plotting logic
````

---

## How to Run

### 1. Clone the Repository

```bash
git clone https://github.com/duaaMansur/Airbnb-Streaming-Analytics.git
cd airbnb-bigdata-project
```

### 2. Start Services with Docker

Make sure Docker is installed and running, then:

```bash
docker-compose up --build
```

This will start:

* Kafka
* Zookeeper
* Cassandra
* (Optionally Spark if configured)

### 3. Set Up Python Environment

Create and activate a virtual environment:

```bash
python3 -m venv env
source env/bin/activate  # On Windows use: env\\Scripts\\activate
pip install -r requirements.txt
```

### 4. Run Streamlit Dashboard

```bash
streamlit run streamlit.py
```

---

## Features

* Real-time insights into:

  * Booking, cancellation, and view actions
  * Average room prices
  * Trends and distributions by location/type
* Identify top hosts, popular room types, and high-cancellation areas

---

## License

This project is intended for academic and educational purposes only.

```



# End-to-End Data Engineering Pipeline 🚀

## Overview
This project is a complete **data engineering pipeline** that covers all stages from ingestion to processing, utilizing technologies like **Apache Airflow**, **Kafka**, **Spark**, and **Cassandra**, all containerized using **Docker** for seamless deployment and scalability.



## Table of Contents
- [Overview](#overview)
- [Project Workflow](#project-workflow)
- [Technologies Used](#technologies-used)


## Project Workflow
1. **Data Ingestion**: Using the [randomuser.me API](https://randomuser.me/) to fetch random user data.
2. **Data Streaming**: Data is streamed from **PostgreSQL** to **Apache Spark** using **Kafka**.
3. **Data Processing**: Spark processes the data in real-time.
4. **Data Storage**: Processed data is stored in **Cassandra**.

## Technologies Used 🛠️
- **Apache Airflow**: Orchestrates the data pipeline
- **Apache Kafka**: Real-time data streaming
- **Apache Spark**: Distributed data processing
- **Cassandra**: Final data storage
- **Docker**: Containerization for deployment
- **PostgreSQL**: Intermediate data storage


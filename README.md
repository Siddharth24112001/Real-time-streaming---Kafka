Overview

This project is a complete data engineering pipeline that covers all stages of data flow from ingestion to processing and finally to storage. The pipeline is built using a modern tech stack that includes Apache Airflow, Apache Kafka, Apache Spark, Cassandra, and other industry-standard tools. The goal is to demonstrate a real-time streaming data workflow with efficient orchestration, processing, and storage solutions. All components are containerized using Docker to ensure ease of deployment and scalability.

Project Architecture

The project consists of the following components:

Data Source: Random user data is generated using the randomuser.me API.
Apache Airflow: Orchestrates the pipeline, handles data fetching, and stores the data temporarily in a PostgreSQL database.
Apache Kafka and Zookeeper: Kafka is used for streaming data from PostgreSQL to the processing engine (Spark). Zookeeper ensures the distributed coordination of Kafka clusters.
Control Center and Schema Registry: Monitors Kafka streams and manages the data schema.
Apache Spark: Processes the incoming data using its distributed computation model, leveraging master and worker nodes.
Cassandra: Serves as the final storage solution for processed data, offering scalability and fault tolerance.
Docker: All components are containerized, allowing for seamless deployment and scalability.
Project Workflow

Data Ingestion: Random user data is generated via the randomuser.me API, and Airflow triggers the ingestion process.
Data Orchestration: Apache Airflow manages the entire pipeline, orchestrating data ingestion, storage, and processing workflows.
Data Streaming: The ingested data is streamed via Apache Kafka from PostgreSQL to Apache Spark for real-time processing.
Data Processing: Apache Spark processes the streamed data, performing necessary transformations and calculations.
Data Storage: The processed data is stored in Cassandra for efficient querying and scalability.
Technologies Used

Apache Airflow: Pipeline orchestration and scheduling
Python: Programming language for integration and scripting
Apache Kafka: Real-time data streaming
Apache Zookeeper: Kafka coordination
Apache Spark: Distributed data processing
Cassandra: Scalable and fault-tolerant database
PostgreSQL: Relational database for intermediate data storage
Docker: Containerization for all components
Control Center & Schema Registry: Kafka monitoring and schema management

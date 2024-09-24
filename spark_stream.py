import logging
from datetime import datetime 

from cassandra.auth import PlainTextAuthProvider
from cassandra.cluster import Cluster
from pyspark.sql import SparkSession
from pyspark.sql.functions import from_json , col

def create_keyspace(session):
    session.execute("""
CREATE KEYSPACE IF NOT EXISTS spark_streams
WITH replication= {'class': 'SimpleStrategy' , 'replication_factor': '1'};
        
                    


def create_table(session):


def insert_data(session, **kwargs):


def create_spark_connection():
    s_conn =  None
    try:
        s_conn = SparkSession.builder\
        .appName('SparkDataStreaming')\
        .config('spark.jars.packages', "com.datastax.spark:spark-cassandra-connector_2.13:3.41", \
                "org.apache.spark:spark-sql-kafka-0-10_2.13.3.4.1") \
        .config('spark.cassandra.connection.host', 'localhost')\
        .getOrCreate()
        
        s_conn.sparkContext.setLogLovel("Error")
        logging.info("Spark connection created successfully")
    except Exception as e:
        logging.error(f"Couldn't create the spark session due to exception {e}")
    return s_conn



def create_cassandra_connection():
    
    try: 
        cluster = Cluster(['localhost'])
        cas_session = cluster.connect()
        return cas_session
    except Exception as e:
        logging.error(f"Couldn't create the cassandra connection due to exception {e}")
        return None




if __name__ == "__main__":
    spark_conn = create_spark_connection()
    if spark_conn is not None: 
        session = create_cassandra_connection
        if session is not None:
            create_keyspace(session)
            create_table(session)

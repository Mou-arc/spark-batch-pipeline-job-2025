from pyspark.sql import SparkSession
from pyspark.sql import functions as F     # To add the timestamp of transformed data
from dotenv import load_dotenv
import os

# 1. Create Spark session with PostgreSQL driver attached
spark = SparkSession.builder.appName("JobTrackingBatchPipeline").master("local[*]").config("spark.jars.packages", "org.postgresql:postgresql:42.7.11").getOrCreate()

spark.sparkContext.setLogLevel("ERROR")

# Connection details
load_dotenv()

db_url = os.environ.get("DB_URL")
db_properties = {
    "user": os.environ.get("DB_USER"),
    "password": os.environ.get("DB_PASSWORD"),
    "driver": "org.postgresql.Driver"
}

# 2. Read data (load data from relational database - PostgreSQL)
#df = spark.read.option("header", "true").option("inferSchema", "true").csv("data/input/sample.csv")     -- when reading from local system
df = spark.read.jdbc(url=db_url, table="job_2025", properties=db_properties)

print("=== Raw Data from job_2025 ===")
df.show()
df.printSchema()

# 3. Transform
#df_clean = df.dropna()      -- drop rows with any null values
df_clean = df.fillna("N/A")
df_result = df_clean.withColumn("processed_at", F.current_timestamp())

print("=== Cleaned Data ===")
df_result.show()

# 4. Write output
#df_result.write.mode("overwrite").parquet("data/output/result")       -- when saving output to local
df_result.write.jdbc(
    url=db_url,
    table="job_2025_pipeline",
    mode="overwrite",
    properties=db_properties
)

print("=== Pipeline complete. Output written to job_2025_pipeline. ===")
spark.stop()

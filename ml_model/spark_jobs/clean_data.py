from pyspark.sql import SparkSession
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv(os.path.join(os.path.dirname(os.path.dirname(__file__)), '../.env'))

# Initialize Spark session
spark = SparkSession.builder \
    .appName("CSV Reader") \
    .getOrCreate()

# Get the local path from environment variable
local_path = os.getenv('LOCAL_PATH')
print(f"Local path: {local_path}")
# Construct the full path to the CSV file
csv_path = os.path.join(local_path, 'discogs.csv')

# Read the CSV file (first 500 rows)
df = spark.read \
    .option("header", "true") \
    .option("inferSchema", "true") \
    .csv(csv_path) \
    .limit(500)

# Show basic information
print("Schema:")
df.printSchema()

print("\nFirst 5 rows:")
df.show(5, truncate=False)

print("\nTotal rows:", df.count())


# Stop Spark session
spark.stop() 
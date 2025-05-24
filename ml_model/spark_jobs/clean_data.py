from pyspark.sql import SparkSession
from pyspark.sql.functions import lit
from pyspark.sql.types import StringType
import os
from dotenv import load_dotenv

# Load environment variables from root .env file
load_dotenv(os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(__file__))), '.env'))

# Set Hadoop home directory
os.environ['HADOOP_HOME'] = 'C:\\hadoop'
os.environ['PATH'] = os.environ['PATH'] + ';C:\\hadoop\\bin'

# Initialize Spark session with current configuration
spark = SparkSession.builder \
    .appName("CSV Cleaner") \
    .config("spark.sql.parquet.datetimeRebaseModeInWrite", "LEGACY") \
    .config("spark.hadoop.fs.defaultFS", "file:///") \
    .config("spark.hadoop.fs.file.impl", "org.apache.hadoop.fs.LocalFileSystem") \
    .getOrCreate()

# Get the local path from environment variable
local_path = os.getenv('LOCAL_PATH')
if not local_path:
    raise ValueError("LOCAL_PATH environment variable not found. Please check your .env file.")

# Construct the full path to the CSV file
csv_path = os.path.join(local_path, 'discogs.csv')

# Read the CSV file
df = spark.read \
    .option("header", "true") \
    .option("inferSchema", "true") \
    .csv(csv_path) \
    .limit(100)  # For testing, remove this in production

# Drop unnecessary columns
df = df.drop('status', 'notes', 'label_id', 'format', 'style', 
             'master_id', 'company_name', 'release_id', 'artist_id', 'video_url')
df = df.withColumn('popularity', lit(None).cast(StringType())) \
       .withColumn('spotify_url', lit(None).cast(StringType())) \
       .withColumn('image_url', lit(None).cast(StringType()))

# Show the cleaned data
print("Cleaned Schema:")
df.printSchema()

print("\nFirst 5 rows of cleaned data:")
df.show(5, truncate=False)

print("\nTotal rows:", df.count())

# Write to CSV using absolute path
output_path = os.path.join(local_path, 'cleaned_discogs.csv')
df.write \
    .mode("overwrite") \
    .option("header", "true") \
    .csv(output_path)

# Stop Spark session
spark.stop() 
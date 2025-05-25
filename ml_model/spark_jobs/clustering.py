from pyspark.sql import SparkSession
from pyspark.ml.feature import StringIndexer, OneHotEncoder, VectorAssembler
from pyspark.ml.clustering import KMeans
from pyspark.sql.functions import col

# Start Spark session
spark = SparkSession.builder.appName("MusicRecommender").getOrCreate()

# Load and clean data
df = spark.read.csv("discog.csv", header=True, inferSchema=True)
df = df.select("title", "artist_id", "genre", "release_date", "country")
df = df.na.drop(subset=["title", "artist_id", "genre", "release_date", "country"])


from pyspark.ml.feature import StringIndexer

# Create StringIndexers and fit them
artist_indexer = StringIndexer(inputCol="artist_id", outputCol="artist_index").fit(df)
genre_indexer = StringIndexer(inputCol="genre", outputCol="genre_index").fit(df)
country_indexer = StringIndexer(inputCol="country", outputCol="country_index").fit(df)

# Transform dataframe with indexers
df_indexed = artist_indexer.transform(df)
df_indexed = genre_indexer.transform(df_indexed)
df_indexed = country_indexer.transform(df_indexed)


df_indexed = df_indexed.withColumn("release_year", col("release_date").cast("double"))

from pyspark.ml.feature import VectorAssembler
df_indexed = df_indexed.na.fill({
    "artist_index": 0.0,
    "genre_index": 0.0,
    "country_index": 0.0,
    "release_year": 0.0
})

assembler = VectorAssembler(
    inputCols=["artist_index", "genre_index", "country_index", "release_year"],
    outputCol="features"
)

df_vector = assembler.transform(df_indexed)

# Train KMeans model
kmeans = KMeans(k=100, seed=42, featuresCol="features", predictionCol="cluster")
try:
    model = kmeans.fit(df_vector)
except Exception as e:
    print(e)
 
# Save everything
artist_indexer.write().overwrite().save("models/artist_indexer")
genre_indexer.write().overwrite().save("models/genre_indexer")
country_indexer.write().overwrite().save("models/country_indexer")
# encoder.write().overwrite().save("models/encoder")
assembler.write().overwrite().save("models/assembler")
model.write().overwrite().save("models/kmeans_model")

print("✅ Model and preprocessing steps saved.")

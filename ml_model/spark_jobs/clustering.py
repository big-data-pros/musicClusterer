from pyspark.sql import SparkSession

spark = SparkSession.builder \
    .appName("Music Recommender") \
    .getOrCreate()

df = spark.read.csv("discog.csv", header=True, inferSchema=True)

from pyspark.sql.functions import col
df = df.select("title", "artist_name", "genre", "release_date", "country")

df = df.na.drop(subset=["title", "artist_name", "genre", "release_date", "country"])

from pyspark.ml.feature import StringIndexer, OneHotEncoder, VectorAssembler

# String Indexing
indexers = [
    StringIndexer(inputCol=col, outputCol=f"{col}_index").fit(df)
    for col in ["artist_name", "genre", "country"]
]

for indexer in indexers:
    df = indexer.transform(df)

# One-Hot Encoding
encoder = OneHotEncoder(
    inputCols=["artist_name_index", "genre_index", "country_index"],
    outputCols=["artist_vec", "genre_vec", "country_vec"]
)
df = encoder.fit(df).transform(df)

# Assemble features
assembler = VectorAssembler(
    inputCols=["artist_vec", "genre_vec", "country_vec", "release_date"],
    outputCol="features"
)
df_vector = assembler.transform(df)

from pyspark.ml.clustering import KMeans

kmeans = KMeans(k=100, seed=42, featuresCol="features", predictionCol="cluster")
model = kmeans.fit(df_vector)
clustered_df = model.transform(df_vector)

# Choose a song
target_song = "The World Of Ray Price"
song_cluster = clustered_df.filter(col("title") == target_song).select("cluster").first()["cluster"]

# Recommend songs from the same cluster
recommendations = clustered_df.filter(col("cluster") == song_cluster).select("title").distinct().limit(5)
recommendations.show()

clustered_df.select("title", "cluster").write.csv("clustered_songs.csv", header=True)

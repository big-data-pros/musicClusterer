from pyspark.ml.clustering import KMeansModel
from pyspark.ml.feature import StringIndexerModel, OneHotEncoderModel, VectorAssembler

# Load saved model and preprocessing steps
artist_indexer = StringIndexerModel.load("models/artist_indexer")
genre_indexer = StringIndexerModel.load("models/genre_indexer")
country_indexer = StringIndexerModel.load("models/country_indexer")
encoder = OneHotEncoderModel.load("models/encoder")
assembler = VectorAssembler.load("models/assembler")
model = KMeansModel.load("models/kmeans_model")

# Load new song(s) for prediction
new_song = spark.createDataFrame([
    ("New Song", "Ray Price", "Folk, World, & Country", 1970.0, "US")
], ["title", "artist_name", "genre", "release_date", "country"])

# Transform using saved preprocessors
new_song = artist_indexer.transform(new_song)
new_song = genre_indexer.transform(new_song)
new_song = country_indexer.transform(new_song)
new_song = encoder.transform(new_song)
new_song = assembler.transform(new_song)

# Predict cluster
result = model.transform(new_song)
result.select("title", "cluster").show()

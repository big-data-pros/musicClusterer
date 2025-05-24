# Music Clusterer

A data processing and clustering project for music data from Discogs and Spotify.

## Project Structure

```
musicClusterer/
├── ml_model/                 # Machine learning and data processing
│   ├── data/                # Processed data files
│   ├── notebooks/           # Jupyter notebooks for analysis
│   ├── spark_jobs/          # PySpark data processing scripts
│   └── spotify_api/         # Spotify API integration
├── flutter_project/         # Flutter mobile application
└── artifacts/              # Generated artifacts and models
```

## Setup

1. Install Python dependencies:

```bash
pip install -r ml_model/requirements.txt
```

2. Set up environment variables in `.env`:

```
CLIENT_ID=your_spotify_client_id
CLIENT_SECRET=your_spotify_client_secret
LOCAL_PATH=/path/to/project/root
```

3. Install Hadoop for Windows:
   - Download Hadoop 3.3.6
   - Extract to `C:\hadoop`
   - Download `winutils.exe` and place in `C:\hadoop\bin`

## Data Processing

The project processes music data from Discogs using PySpark:

1. Clean and preprocess data:

```bash
python ml_model/spark_jobs/clean_data.py
```

2. Fetch additional data from Spotify:

```bash
python ml_model/spotify_api/fetch_info.py
```

## Features

- Large-scale data processing with PySpark
- Spotify API integration for additional metadata
- Data cleaning and deduplication
- Mobile app interface (Flutter)

## Data Sources

- Discogs dataset (discogs.csv)
- Spotify API for additional metadata

## Development

- Python 3.12
- PySpark for data processing
- Flutter for mobile app
- Spotify Web API

class TrackModel {
  final String id;
  final String title;
  final String artistName;
  final String spotifyUrl;
  final String imageUrl;

  TrackModel({
    required this.id,
    required this.title,
    required this.artistName,
    required this.spotifyUrl,
    required this.imageUrl,
  });

  @override
  String toString() {
    return 'TrackModel(id: $id, title: $title, artistName: $artistName, spotifyUrl: $spotifyUrl, imageUrl: $imageUrl)';
  }
}

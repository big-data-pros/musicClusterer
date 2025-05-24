import 'package:flutter/material.dart';
import 'package:flutter_project/core/dummy/dummy.dart';
import 'package:flutter_project/core/models/track_model.dart';
import 'package:flutter_project/core/constants/app_colors.dart';
import 'package:url_launcher/url_launcher.dart';

class LikesPage extends StatefulWidget {
  const LikesPage({super.key});

  @override
  State<LikesPage> createState() => _LikesPageState();
}

class _LikesPageState extends State<LikesPage> {
  List<TrackModel> tracks = Dummy.getDummyTracks();
  TrackModel selectedTrack = Dummy.getDummyTracks()[0];
  Future<void> _launchSpotifyUrl(String url) async {
    final Uri uri = Uri.parse(url);
    if (!await launchUrl(uri, mode: LaunchMode.externalApplication)) {
      ScaffoldMessenger.of(context).showSnackBar(
        const SnackBar(content: Text('Could not open Spotify')),
      );
    }
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      backgroundColor: AppColors.backgroundDark,
      appBar: AppBar(
        backgroundColor: AppColors.backgroundDark,
        elevation: 0,
        leading: IconButton(
          icon: const Icon(Icons.arrow_back, color: AppColors.textPrimaryColor),
          onPressed: () => Navigator.of(context).pop(),
        ),
        title: const Text(
          'Home',
          style: TextStyle(color: AppColors.textPrimaryColor),
        ),
      ),
      body: Column(
        crossAxisAlignment: CrossAxisAlignment.start,
        children: [
          Padding(
            padding: const EdgeInsets.all(16.0),
            child: Row(
              children: [
                SizedBox(
                  width: 100,
                  height: 100,
                  child: GridView.builder(
                    physics: const NeverScrollableScrollPhysics(),
                    gridDelegate:
                        const SliverGridDelegateWithFixedCrossAxisCount(
                      crossAxisCount: 2,
                      mainAxisSpacing: 2,
                      crossAxisSpacing: 2,
                    ),
                    itemCount: 4,
                    itemBuilder: (context, index) {
                      return Image.network(
                        selectedTrack.imageUrl,
                        fit: BoxFit.cover,
                      );
                    },
                  ),
                ),
                const SizedBox(width: 16),
                Expanded(
                  child: Column(
                    crossAxisAlignment: CrossAxisAlignment.start,
                    children: [
                      Text(
                        selectedTrack.title,
                        style: TextStyle(
                          fontSize: 20,
                          fontWeight: FontWeight.bold,
                          color: AppColors.textPrimaryColor,
                        ),
                      ),
                      SizedBox(height: 4),
                      Text(
                        selectedTrack.artistName,
                        style: TextStyle(color: AppColors.textError),
                      ),
                    ],
                  ),
                ),
              ],
            ),
          ),

          // Open Spotify Button
          Padding(
            padding: const EdgeInsets.symmetric(horizontal: 16.0),
            child: ElevatedButton.icon(
              style: ElevatedButton.styleFrom(
                backgroundColor: AppColors.successColor,
                padding: const EdgeInsets.symmetric(vertical: 14),
              ),
              onPressed: () {
                _launchSpotifyUrl(selectedTrack.spotifyUrl);
              },
              icon: const Icon(Icons.open_in_new, color: Colors.black),
              label: const Text(
                'Open Spotify',
                style: TextStyle(color: Colors.black),
              ),
            ),
          ),

          const SizedBox(height: 10),

          const Divider(color: AppColors.borderColor),

          Expanded(
            child: ListView.separated(
              itemCount: tracks.length,
              separatorBuilder: (context, index) =>
                  const Divider(color: AppColors.borderColor),
              itemBuilder: (context, index) {
                final track = tracks[index];
                return Dismissible(
                  key: Key(track.id),
                  direction: DismissDirection.endToStart,
                  background: Container(
                    color: AppColors.errorColor,
                    alignment: Alignment.centerRight,
                    padding: const EdgeInsets.symmetric(horizontal: 20),
                    child: const Icon(Icons.delete, color: Colors.white),
                  ),
                  onDismissed: (direction) {
                    setState(() {
                      tracks.removeAt(index);
                    });
                    ScaffoldMessenger.of(context).showSnackBar(
                      const SnackBar(content: Text('Track removed')),
                    );
                  },
                  child: ListTile(
                      leading: ClipRRect(
                        borderRadius: BorderRadius.circular(8),
                        child: Image.network(
                          track.imageUrl,
                          width: 50,
                          height: 50,
                          fit: BoxFit.cover,
                        ),
                      ),
                      title: Text(track.title,
                          style: const TextStyle(
                              color: AppColors.textPrimaryColor)),
                      subtitle: Text(track.artistName,
                          style: const TextStyle(color: AppColors.textMuted)),
                      onTap: () {
                        setState(() {
                          selectedTrack = track;
                        });
                      }),
                );
              },
            ),
          ),
        ],
      ),
      bottomNavigationBar: BottomNavigationBar(
        backgroundColor: AppColors.backgroundDarker,
        selectedItemColor: AppColors.textError,
        unselectedItemColor: AppColors.textPrimaryColor,
        items: const [
          BottomNavigationBarItem(icon: Icon(Icons.home), label: 'Home'),
          BottomNavigationBarItem(
              icon: Icon(Icons.library_music), label: 'Browse'),
          BottomNavigationBarItem(icon: Icon(Icons.search), label: 'Search'),
          BottomNavigationBarItem(icon: Icon(Icons.person), label: 'User'),
        ],
        currentIndex: 0,
        onTap: (index) {},
      ),
    );
  }
}

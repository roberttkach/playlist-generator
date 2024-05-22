import os

def create_playlist(directory):
    playlist = []
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith(".mp3"):
                playlist.append(os.path.join(root, file))
    return playlist

directory = "/path/to/your/favorite/songs"
playlist = create_playlist(directory)

for song in playlist:
    print(song)

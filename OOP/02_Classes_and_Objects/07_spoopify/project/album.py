from typing import List

from project import Song

class Album:
    def __init__(self, name: str, *songs: Song):
        self.name = name
        self.songs: List[Song] = list(songs)
        self.published = False

    def add_song(self, song: Song):
        if song.single:
            return f"Cannot add {song.name}. It's a single"

        if self.published:
            return "Cannot add songs. Album is published."

        if any(s.name == song.name for s in self.songs):
            return "Song is already in the album."

        self.songs.append(song)
        return f"Song {song.name} has been added to the album {self.name}."

    def remove_song(self, song_name: str):
        if self.published:  # ✅ First, check if the album is published
            return "Cannot remove songs. Album is published."

        for song in self.songs:  # ✅ Iterate through the songs
            if song.name == song_name:  # ✅ If song matches, remove it
                self.songs.remove(song)
                return f"Removed song {song_name} from album {self.name}."

        return "Song is not in the album."  # ✅ If loop finishes without finding the song

    def publish(self):
        if self.published:
            return f"Album {self.name} is already published."
        self.published = True
        return f"Album {self.name} has been published."


    def details(self):
        result = f"Album {self.name}\n"  # Start with the album name
        result += "\n".join(f"== {song.get_info()}" for song in self.songs)  # Add song details
        return result
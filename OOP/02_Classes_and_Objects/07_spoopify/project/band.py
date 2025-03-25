from typing import List

from project import Album
from project import Song


class Band:
    def __init__(self, name: str):
        self.name = name
        self.albums: List[Album] = []

    def add_album(self, album: Album):
        if any(a.name == album.name for a in self.albums):
            return f"Band {self.name} already has {album.name} in their library."

        # alternative approach:
        #  for a in self.albums:
        # if a.name == album.name:
        #     return f"Band {self.name} already has {album.name} in their library."


        self.albums.append(album)
        return f"Band {self.name} has added their newest album {album.name}."

    def remove_album(self, album_name: str):
        for a in self.albums:
            if a.name == album_name:  # ✅ Find the correct Album object
                if a.published:
                    return "Album has been published. It cannot be removed."
                self.albums.remove(a)
                return f"Album {album_name} has been removed."

        return f"Album {album_name} is not found."  # ✅ Only return t


    def details(self):
        result = f"Band {self.name}\n"
        result += "\n".join(f"{album.details()}" for album in self.albums)
        return result
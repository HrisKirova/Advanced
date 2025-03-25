import math


class PhotoAlbum:
    def __init__(self, pages: int):
        self.pages = pages
        self.photos: list = [[] for _ in range(self.pages)]

    @classmethod
    def from_photos_count(cls, photos_count: int):
        pages_needed = math.ceil(photos_count / 4)
        return cls(pages_needed)

    def add_photo(self, label: str):
        for page_index in range(self.pages):
            if len(self.photos[page_index]) < 4:  # Check if the page has space
                self.photos[page_index].append(label)  # Add photo
                slot_number = len(self.photos[page_index])  # Slot position
                return f"{label} photo added successfully on page {page_index + 1} slot {slot_number}"

        return "No more free slots"

    def display(self):
        result = ["-----------"]  # ✅ Start with the first separator

        for page in self.photos:
            photos_on_page = " ".join("[]" for _ in page)  # ✅ Convert photos to "[]"
            result.append(photos_on_page if photos_on_page else "")  # ✅ Add blank line for empty pages
            result.append("-----------")  # ✅ Page separator

        return "\n".join(result)  # ✅ Convert the list to a string with new lines


album = PhotoAlbum(2)

print(album.add_photo("baby"))
print(album.add_photo("first grade"))
print(album.add_photo("eight grade"))
print(album.add_photo("party with friends"))
print(album.photos)
print(album.add_photo("prom"))
print(album.add_photo("wedding"))

print(album.display())

def classify_books(*book_tuples, **isbn_books):
    fiction_books = {}
    non_fiction_books = {}


    for genre, title in book_tuples:
        if genre == "fiction":
            for isbn, book_title in isbn_books.items():
                if book_title == title:
                    fiction_books[isbn] = book_title
        elif genre == "non_fiction":
            for isbn, book_title in isbn_books.items():
                if book_title == title:
                    non_fiction_books[isbn] = book_title


    sorted_fiction = sorted(fiction_books.items())
    sorted_non_fiction = sorted(non_fiction_books.items(), reverse=True)


    result = []
    if sorted_fiction:
        result.append("Fiction Books:")
        for isbn, title in sorted_fiction:
            result.append(f"~~~{isbn}#{title}")

    if sorted_non_fiction:
        result.append("Non-Fiction Books:")
        for isbn, title in sorted_non_fiction:
            result.append(f"***{isbn}#{title}")

    return "\n".join(result)

print(classify_books(
    ("fiction", "Brave New World"),
    ("non_fiction", "The Art of War"),
    NF3421NN="The Art of War",
    FF1234UU="Brave New World"
))

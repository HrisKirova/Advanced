from typing import final


def concatenate(*args, **kwargs):
    new_text = ""
    for text in args:
        new_text += text
    for key, value in kwargs.items():
        if key in new_text:
            new_text = new_text.replace(key, value)
    return new_text

print(concatenate("Soft", "UNI", "Is", "Grate", "!", UNI="Uni", Grate="Great"))
print(concatenate("I", " ", "Love", " ", "Cythons", C="P", s="", java='Java'))
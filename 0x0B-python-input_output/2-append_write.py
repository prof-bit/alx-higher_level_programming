#!/usr/bin/python3i
def append_write(filename="", text=""):
    """Appends a string at the end of a UTF-8 text file and returns the number of characters added."""
    with open(filename, "a", encoding="utf-8") as file:
        characters_added = file.write(text)
        return characters_added

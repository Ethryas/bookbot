def get_book_text(file):
    path_to_file = file
    with open(path_to_file, 'r') as file:
        file_contents = file.read()
        return file_contents

def count_words(text):
    words = len(text.split())
    print(f"Found {words} total words")
    return

def count_characters(text):
    lowercase_text = text.lower()
    characters = {"a": 0, "b": 0, "c": 0, "d": 0, "e": 0, "f": 0, "g": 0, "h": 0, "i": 0,
    "j": 0, "k": 0, "l": 0, "m": 0, "n": 0, "o": 0, "p": 0, "q": 0, "r": 0, "s": 0, "t": 0,
    "u": 0, "v": 0, "w": 0, "x": 0, "y": 0, "z": 0, " ": 0, ",": 0, ".": 0, ";": 0, ":": 0}
    for char in lowercase_text:
        if char in characters:
            characters[char] += 1
    return characters


def sort_characters(characters):
    def sort_key(item):
        return item["num"]
    # Initialize empty list to store dictionaries
    char_list = []
    
    for k, v in characters.items():
        # Create a dictionary for each character
        char_dict = {"char": k, "num": v}
        char_list.append(char_dict)
    char_list.sort(key=sort_key, reverse=True)
    return char_list
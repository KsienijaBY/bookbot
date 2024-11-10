import os

def get_book_text(path):
    full_path = os.path.join(os.getcwd(), path)
    print(f"Attempting to open file at: {full_path}") 
    with open(full_path) as f:
        return f.read()

def count_words(text):
    words = text.split()
    return len(words)

def count_char(text):
    text = text.lower()
    char_count = {}
    for char in text:
        if char not in char_count:
            char_count[char] = 1
        else:
            char_count[char] += 1
    return(char_count)

def sort_on(dict):
    return dict["num"]

def list_of_dict(char_count):
    char_list = []
    for char in char_count:
        new_dict = {"char": char, "num": char_count[char]}
        char_list.append(new_dict)
    char_list.sort(reverse=True, key=sort_on)  # This does the actual sorting
    return char_list

def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    word_count = count_words(text)
    char_count = count_char(text)

    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{word_count} words found in the document\n")

    char_list = list_of_dict(char_count)
    for item in char_list:
        if item['char'].isalpha():  # Only print alphabetic characters
            print(f"The '{item['char']}' character was found {item['num']} times")

    print("--- End report ---")


if __name__ == "__main__":
    main()





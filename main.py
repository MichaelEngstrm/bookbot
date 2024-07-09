def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    char_dict = get_chars_dict(text)
    alpha_list = get_alpha_dict(char_dict)

    write_book_report(book_path, num_words, alpha_list)

def get_book_text(path):
    with open(path) as t:
        return t.read()
        
def get_num_words(text):
    return len(text.split())

def get_chars_dict(text):
    character_count = {}

    for c in text:
        lowered = c.lower()
        if lowered in character_count:
            character_count[lowered] += 1
        else:
            character_count[lowered] = 1

    return character_count

def get_alpha_dict(char_dict):
    alpha_dict = []
    for char in char_dict:
        if char.isalpha():
            d = {'letter': char, 'num': char_dict[char]}
            alpha_dict.append(d)

    return alpha_dict

def write_book_report(book, num_words, letters):
    letters.sort(reverse=True, key=sort_on)
    print(f"--- Begin report of {book} ---")
    print(f"{num_words} words was found in the book\n")
    
    for c in letters:
        print(f"the '{c['letter']}' character was found '{c['num']}' times")

    print("--- End report ---")

def sort_on(dict):
    return dict["num"]

main()
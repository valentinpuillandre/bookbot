
def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = word_count(text)
    num_characters = characters_count(text)
    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{num_words} words found in the document")
    for key, value in num_characters.items():
        print(f"The '{key}' character was found {value} times")
    print("--- End report ---")


def get_book_text(path):
    with open(path) as f:
        return f.read()

def word_count(text):
    return len(text.split())

def characters_count(text):
    text = text.lower()
    chr_count = {}
    for elem in text:
        if elem in ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]:
            if elem in chr_count:
                chr_count[elem] += 1
            else:
                chr_count[elem] = 1
        else:
            pass
    return chr_count


main()
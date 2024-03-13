def main():   
    words = []
    letters = {} 
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        lowerString = file_contents.lower()
        for letter in lowerString:
            if letter in letters:
                letters[letter] += 1
            else:
                letters[letter] = 1
        words = file_contents.split()
        print(f"{len(words)} words found in the document")

    sorted_letters_by_occurance = sorted(letters.items(), key=lambda x:x[1], reverse=True)
    sorted_letters = dict(sorted_letters_by_occurance)

    for letter in sorted_letters:
        if letter in "abcdefghijklmnopqrstuvwxyz":
            print(f"The '{letter}' character was found {letters[letter]} times")
    print("--- End report ---")
main
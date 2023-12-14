def main():
    input_file_path = "common_words.txt"
    output_file_path = "easy_hangman_words.txt"
    five_letter_words = []

    with open(input_file_path, "r") as f:
        for line in f.readlines():
            word = line.strip()
            if word.isalpha():
                if len(word) >= 4 and len(word) <= 6:
                    if word not in five_letter_words:
                        five_letter_words.append(word)
            else:
                pass
    with open(output_file_path, "w") as f:
        for word in five_letter_words:
            f.write(word + "\n")

    print(f"Found {len(five_letter_words)} five-letter words.")


if __name__ == "__main__":
    main()
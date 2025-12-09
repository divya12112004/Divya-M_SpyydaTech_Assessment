# Word Frequency Counter Program

def word_frequency_counter(text):
    # Convert text to lowercase
    text = text.lower()

    # Remove common punctuation marks
    punctuations = [",", ".", "!", "?", ";", ":", "(", ")", "\"", "'"]
    for p in punctuations:
        text = text.replace(p, " ")

    # Split text into words
    words = text.split()

    # Dictionary to count each word
    word_count = {}

    for w in words:
        if w in word_count:
            word_count[w] += 1
        else:
            word_count[w] = 1

    # Sort by frequency in descending order
    sorted_words = sorted(word_count.items(), key=lambda x: x[1], reverse=True)

    # Display output
    print("\nWord Frequency:\n")
    for word, count in sorted_words:
        print(f"{word} - {count}")


def main():
    # User input
    text = input("Enter a paragraph: ").strip()

    if text == "":
        print("No input provided!")
    else:
        word_frequency_counter(text)


if __name__ == "__main__":
    main()

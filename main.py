text = input("Enter your text: ")

def count_words(text):
    text_count = len(text.split())
    words = text.split()
    return text_count, words

print(count_words(text))
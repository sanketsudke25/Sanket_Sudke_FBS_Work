# Function to count word occurrences
def count_word_occurrences(text):
    word_counts = {}
    words = text.split()

    for word in words:
        word = word.lower()  
        word_counts[word] = word_counts.get(word, 0) + 1

    return word_counts
input_string = input("Enter a string: ")
result = count_word_occurrences(input_string)
print("Word occurrences:")
for word, count in result.items():
    print(f"{word}: {count}")
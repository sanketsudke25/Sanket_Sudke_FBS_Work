string_list = ["Python is easy to learn","Python is powerful","Learn Python step by step"]
all_words = []
for sentence in string_list:
    words = sentence.lower().split()
    all_words.extend(words)
unique_words = set(all_words)
word_freq = {}
for word in unique_words:
    word_freq[word] = all_words.count(word)
print("Unique Words:", unique_words)
print("Word Frequencies:")
for word, freq in word_freq.items():
    print(f"{word}: {freq}")
input_str = "Python is powerful and Python is easy to learn"
words = input_str.lower().split()

word_freq = {}
for word in words:
    if word in word_freq:
        word_freq[word] += 1
    else:
        word_freq[word] = 1
print("Word Frequency Dictionary:")
print(word_freq)
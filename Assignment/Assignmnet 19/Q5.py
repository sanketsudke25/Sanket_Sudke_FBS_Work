user = input("Enter a sentence: ")
short_words = [word for word in user.split() if len(word) < 5]
print("Words with less than 5 letters:", short_words)
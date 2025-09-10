input_string = input("Enter a string: ")

char_count = 0
word_count = 0
in_word = False

for ch in input_string:
    char_count += 1  
    if ch != ' ' and not in_word:
        word_count += 1
        in_word = True
    elif ch == ' ':
        print("Number of characters:", char_count)
print("Number of words:", word_count)
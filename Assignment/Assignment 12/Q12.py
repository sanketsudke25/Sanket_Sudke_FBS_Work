def count_lowercase(text):
    count = 0
    for char in text:
        if char.islower():
            count += 1
    return count
input_string = input("Enter a string: ")
lowercase_count = count_lowercase(input_string)
print("Number of lowercase characters:", lowercase_count)
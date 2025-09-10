def count_digits_and_letters(text):
    digit_count = 0
    letter_count = 0

    for char in text:
        if char.isdigit():
            digit_count += 1
        elif char.isalpha():
            letter_count += 1

    return digit_count, letter_count
input_string = input("Enter a string: ")
digits, letters = count_digits_and_letters(input_string)
print("Number of digits:", digits)
print("Number of letters:", letters)
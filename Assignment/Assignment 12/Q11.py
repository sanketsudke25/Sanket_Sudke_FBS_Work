def replace_spaces_with_hyphen(text):
    return text.replace(' ', '-')
input_string = input("Enter a string: ")
output_string = replace_spaces_with_hyphen(input_string)
print("Modified string:", output_string)
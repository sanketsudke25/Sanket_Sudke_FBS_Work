input_string = input("Enter a string: ")
result = ""
for i in range(0, len(input_string)):
    if i % 2 == 0:  
        result += input_string[i]
print("String after removing odd index characters:", result)
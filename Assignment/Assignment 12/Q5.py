input_string = input("Enter a string: ")

vowel_list = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']

count = 0


for i in range(0, len(input_string)):

    for j in range(0, len(vowel_list)):
        if input_string[i] == vowel_list[j]:
            count += 1
            break  
print("Number of vowels in the string:", count)
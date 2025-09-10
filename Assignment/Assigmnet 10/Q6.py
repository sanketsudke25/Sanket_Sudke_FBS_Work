numbers = [1, 2, 2, 3, 4, 4, 5, 1]

unique_numbers = []

for num in numbers:
    if num not in unique_numbers:
        unique_numbers.append(num)


print("Original list:", numbers)
print("List after removing duplicates:", unique_numbers)
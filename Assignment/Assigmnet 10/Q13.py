numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

odd_numbers = []
for num in numbers:
    if (num % 2 != 0):
        odd_numbers.append(num)

print("Original list:", numbers)
print("List after removing even numbers:", odd_numbers)
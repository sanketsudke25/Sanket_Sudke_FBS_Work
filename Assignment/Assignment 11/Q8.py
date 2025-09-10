numbers = [1, 2, 3, 4, 5]

print("Original list:", numbers)

numbers.append(6)
print("After appending 6:", numbers)

numbers.remove(3)
print("After removing 3:", numbers)
print("First element:", numbers[0])
print("Last element:", numbers[-1])

print("All elements:")
for num in numbers:
    print(num)

print("Length of the list:", len(numbers))
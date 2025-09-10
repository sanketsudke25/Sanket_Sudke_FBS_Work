numbers = [10, 15, 22, 33, 40, 55, 60, 73, 88]

even_list = []
odd_list = []

for num in numbers:
    if (num % 2 == 0):
        even_list.append(num)
    else:
        odd_list.append(num)

print("Original list:", numbers)
print("Even numbers:", even_list)
print("Odd numbers:", odd_list)
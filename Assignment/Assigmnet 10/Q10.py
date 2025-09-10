numbers = [1, 2, 3, 2, 4, 2, 5]

remove_element = 2

new_list = []
for num in numbers:
    if (num != remove_element):
        new_list.append(num)


print("Original list:", numbers)
print("List after removing", remove_element, ":", new_list)
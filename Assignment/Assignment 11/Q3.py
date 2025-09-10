data = [[1, 5], [3, 2], [4, 8], [2, 4]]

sorted_data = sorted(data, key=lambda x: x[1])


print("Original list:", data)
print("Sorted list by second element:", sorted_data)
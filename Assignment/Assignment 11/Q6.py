list1 = [1, 2, 3, 4]
list2 = [3, 4, 5, 6]
union_list = []

for item in list1:
    if (item not in union_list):
        union_list.append(item)

for item in list2:
    if (item not in union_list):
        union_list.append(item)


print("List 1:", list1)
print("List 2:", list2)
print("Union of both lists:", union_list)
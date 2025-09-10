def union_lists(li1, li2):
    union = []

    for i in li1:
        if (i not in union):
            union.append(i)

    for j in li2:
        if (j not in union):
            union.append(j)

    return union
li1 = [1,2,3,4,5]
li2 = [3,4,5,6,7]

result = union_lists(li1, li2)
print("Union of the two lists:", result)


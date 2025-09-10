#a list contains sublist with emp info as follows:- li = [[101,"seema",45000],[340,"ranani",13000],[210,"tannu",14000],[320,"suresh",35000]] write a program to sort the list base on salary


li = [[101, "seema", 45000], [340, "ranani", 13000], [210, "tannu", 14000], [320, "suresh", 35000]]

sorted_li = sorted(li, key=lambda x:x [2])

print("Sorted list based on salary:")
for emp in sorted_li:
    print(emp)
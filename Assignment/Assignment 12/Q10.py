string1 = input("Enter the first string: ")
string2 = input("Enter the second string: ")

length1 = 0
length2 = 0
for ch in string1:
    length1 += 1
for ch in string2:
    length2 += 1
if length1 > length2:
    print("The larger string is:", string1)
elif length2 > length1:
    print("The larger string is:", string2)
else:
    print("Both strings are equal in length.")
def manual_length(s):
    count = 0
    for _ in s:
        count += 1
    return count

def find_larger_string(str1, str2):
    len1 = manual_length(str1)
    len2 = manual_length(str2)

    if len1 > len2:
        return str1
    elif len2 > len1:
        return str2
    else:
        return "Both strings are equal in length."
string1 = input("Enter first string: ")
string2 = input("Enter second string: ")

result = find_larger_string(string1, string2)
print("Larger string:", result)
str1 = input("Enter first string: ")
str2 = input("Enter second string: ")

str1 = str1.replace(" ", "")
str2 = str2.replace(" ", "")

if sorted(str1) == sorted(str2):
    print("The strings are anagrams.")
else:
    print("The strings are not anagrams.")
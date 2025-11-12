user= input("Enter a string: ")
vowels = 'aeiou'
no_vowels = ''.join([char for char in user if char not in vowels])
print("String without vowels:", no_vowels)

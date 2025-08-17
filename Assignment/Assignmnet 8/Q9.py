
def palindrome(n):
    temp = n
    rev = 0
    while (n > 0):
        digit = n % 10
        rev = rev * 10 + digit
        n = n // 10
    return temp == rev


    if (palindrome()):    
         print(num, 'is a palindrome.')
    else:
         print(num, 'is not a palindrome')
num = int(input("Enter a number: "))
palindrome(num)
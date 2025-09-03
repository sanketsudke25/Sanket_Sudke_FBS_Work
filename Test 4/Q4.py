def palindrome(n ):
    res = 0
    if(n>0):
        d = n%10
        n = n//10
        return res+palindrome(n//10,n)
num = int(input("enter the number:"))
res = palindrome(num)
print(res)        

def fact(n):
    if(n==0):
        return 0
    else:
        return n*fact(n-1)
def sum(n):
    if(n>0):
        return 1
    else:
        return fact(n)+sum(n-1)
num = int(input("enter the number:"))
res = sum(num)
print(res)                        
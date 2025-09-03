def sos(n):
    if(n==0):
        return 0
    else:
        return  n + sos(n-1)
n=5
sum = sos(n)
print(sum)            

def reverse(num,res=0):
    if(num ==0):
        return res 
    else:
        digits = num%10
        res =res*10+digits
        return reverse(num//10,res)
n=int(input("enter the number"))
reversed_num=reverse(n)
print("Reversed number:", reversed_num)           
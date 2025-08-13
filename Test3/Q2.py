num = int(input("enter the number"))
value= 1
fact = 1
for i in range(1, num + 1):
    fact *= i
    value += value // fact
  
print(f'{value}')


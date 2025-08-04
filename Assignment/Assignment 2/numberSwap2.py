#without using 3rd variable

x = int(input("Enter the value:"))
y = int(input("Enter the value:"))


x = x+y
y = x-y
x = x-y


print(f'number swaiping x:{x} y:{y}. ')



#x,y=y,x

x = int(input("Enter the value of x:"))
y = int(input("Enter the value of y:"))


x,y = y,x
print(f'number swaping {x} {y}. ')
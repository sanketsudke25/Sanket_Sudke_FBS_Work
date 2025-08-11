# Program to print Fibonacci series form user

n = int(input("Enter number : "))
a = 0
b= 1

print("Fibonacci series:")
for i in range(n):
      c =a+b
      print(c, end=" ")
      a = b
      b= c
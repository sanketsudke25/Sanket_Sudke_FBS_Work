# Program to print all odd numbers until n

n = int(input("Enter a number: "))

for i in range(1, n + 1):
    if (i % 2 != 0):
      print(i ,end=' ')
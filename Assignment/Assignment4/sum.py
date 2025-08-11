# Program to find the sum of series from 1 to n

n = int(input("Enter a number: "))
total = 0

for i in range(1, n + 1):
    print(i)
    total += i

print("Sum of series:", total)
def fibonacci_series(n):
    a = 1
    b = 1 
    print(a, end=' ')
    if (n > 1):
        print(b, end=' ')
    for i in range(3, n + 1):
        c = a + b
        print(c, end=' ')
        a = b
        b = c

n = int(input("Enter the number : "))
if (n <= 0):
    print(" enter a positive integer.")
else:
    print("Fibonacci series:")
    fibonacci_series(n)

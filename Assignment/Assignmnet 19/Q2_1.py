def fibonacci_generator(limit):
    a, b = 0, 1
    while (a <= limit):
        yield a
        a, b = b, a + b

limit = int(input("Generate Fibonacci numbers up to: "))
for num in fibonacci_generator(limit):
    print(num)
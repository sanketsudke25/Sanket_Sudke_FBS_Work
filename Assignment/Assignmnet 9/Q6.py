def fibo(n, a, b):
    if(n > 0):
        c = a + b
        print(c)
        fibo(n - 1, b, c)
num = 20
a = -1
b = 1
fibo(num, a, b)        
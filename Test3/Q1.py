n = int(input("enter first prime numbers: "))

count = 0     
num = 2       

print(f"First {n} prime numbers:")

while (count < n):
    prime = True

    for i in range(2, num):
        if (num % i == 0):
            prime = False
            break
    if (prime):
        print(num)
        count += 1

    num += 1
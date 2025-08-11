num = int(input("Enter a number: "))
divisors = 0


for i in range(1, num):
    if (num % i == 0):
        divisors += i


if (divisors == num):
    print(num, "is a Perfect Number")
else:
    print(num, "is not a Perfect Number")
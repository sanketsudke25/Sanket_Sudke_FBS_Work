def armstrong(n, num):
    if (n == 0):
        return 0
    return (n % 10) ** num + armstrong(n // 10, num)

num = int(input("Enter a number: "))
temp = num
digits = 0
while (temp > 0):
    digits += 1
    temp //= 10

print("Number of digits:", digits)

if (armstrong(num, digits) == num):
    print("Armstrong number")
else:
    print("Not an Armstrong number")
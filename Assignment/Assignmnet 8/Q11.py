def armstrong():
    sum = 0
    temp = num
    while (temp > 0):
        sum += 1
        temp = temp // 10

    total = 0
    temp = num
    while (temp > 0):
        digit = temp % 10
        total += digit ** sum
        temp = temp // 10

    return total == num

num = int(input("Enter the number: "))
if (armstrong()):
    print(f"{num} is an Armstrong number.")
else:
    print(f"{num} is NOT an Armstrong number.")
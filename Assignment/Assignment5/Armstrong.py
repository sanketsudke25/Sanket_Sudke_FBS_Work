
num = int(input("Enter a number: "))
original = num
count = 0
temp = num
while (temp > 0):
    count += 1
    temp //= 10
sum = 0
temp = num
while (temp > 0):
    digit = temp % 10
    sum += digit ** count
    temp //= 10
if (sum == original):
    print("It is an Armstrong number.")
else:
    print("It is not an Armstrong number.")
    
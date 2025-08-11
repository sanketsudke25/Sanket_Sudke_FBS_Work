# Check if a single number is Armstrong
num = int(input("Enter the number: "))

range = str(num)
power = len(range)

total = 0
for d in str(num):

    total += int(d) ** power

if total == num:
    print(f"{num} is an Armstrong number.")
else:
    print(f"{num} is NOT an Armstrong number.")
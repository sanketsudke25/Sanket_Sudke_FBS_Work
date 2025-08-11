# Function to calculate factorial using loop

num = int(input("Enter the number: "))
add = 0
temp = num

while (temp > 0):
    d = temp % 10
    temp = temp // 10

    fact = 1
    for i in range(1, d + 1):
        fact *= i

    add += fact

if (add == num):
    print(f"Strong number is {num}")
else:
    print("Not a strong number")
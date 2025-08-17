
def sum(n):
    return (n * (n + 1) // 2)


def factorial(x):
    result = 1
    for i in range(1, x + 1):
        result *= i
    return result

def sum_factorials(n):
    total = 0
    for i in range(1, n + 1):
        total += factorial(i)
    return total

def sum_powers(n):
    total = 0
    for i in range(1, n + 1):
        total += i ** i
    return total


n = int(input("Enter the value of n: "))


print(f"a. {sum(n)}")
print(f"b. {sum_factorials(n)}")
print(f"c. {sum_powers(n)}")
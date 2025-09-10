numbers = [10, 15, 20, 30, 40, 45, 60, 75, 90]

m = 5
n = 10
divisible_by_m_and_n = []

for num in numbers:
    if (num % m == 0 and num % n == 0):
        divisible_by_m_and_n.append(num)
print("Original list:", numbers)
print(f"Numbers divisible by {m} and {n}:", divisible_by_m_and_n)
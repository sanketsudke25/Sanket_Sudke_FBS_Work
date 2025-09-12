numbers = [2, 4, 3, 5, 7, 8, -1]
target_sum = 7
pairs = []
for i in range(len(numbers)):
    for j in range(i + 1, len(numbers)):
        if numbers[i] + numbers[j] == target_sum:
            pairs.append((numbers[i], numbers[j]))
print(f"Pairs with sum {target_sum}:")
for pair in pairs:
    print(pair)
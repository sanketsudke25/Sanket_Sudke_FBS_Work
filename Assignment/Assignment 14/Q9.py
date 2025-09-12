numbers = [1, 2, -1, 0, 3, -2, 4]
target_sum = 3

triplets = set()
numbers.sort()
for i in range(len(numbers)):
    for j in range(i + 1, len(numbers)):
        for k in range(j + 1, len(numbers)):
            if numbers[i] + numbers[j] + numbers[k] == target_sum:
                triplet = tuple(sorted((numbers[i], numbers[j], numbers[k])))
                triplets.add(triplet)
print(f"Unique triplets that sum to {target_sum}:")
for t in triplets:
    print(t)
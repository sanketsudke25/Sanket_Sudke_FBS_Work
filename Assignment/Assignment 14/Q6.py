numbers = [3, 5, -10, 8, -20, 7]
unique_numbers = set(numbers)

num_list = list(unique_numbers)
max_product = float('-inf')
max_pair = ()

for i in range(len(num_list)):
    for j in range(i + 1, len(num_list)):
        product = num_list[i] * num_list[j]
        if product > max_product:
            max_product = product
            max_pair = (num_list[i], num_list[j])
print("Pair with maximum product:", max_pair)
print("Maximum product:", max_product)
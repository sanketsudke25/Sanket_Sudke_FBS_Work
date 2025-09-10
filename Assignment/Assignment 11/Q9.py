numbers = list(range(1, 11))
squares = []
for num in numbers:
    squares.append(num ** 2)

cubes = []
for num in numbers:
    cubes.append(num ** 3)


print("Number,Square,Cube")
for i in range(len(numbers)):
    print(f"{numbers[i]}, {squares[i]}, {cubes[i]}")
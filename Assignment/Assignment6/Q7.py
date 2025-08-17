k = 5

for i in range(1, k + 1):
    
    for j in range(k - i):
        print(' ', end=' ')

    for j in range(1, 2*i):
        print(chr(64 + j), end=' ')
    print()



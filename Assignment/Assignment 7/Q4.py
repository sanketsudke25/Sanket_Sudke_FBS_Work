k = 8
for i in range(1, 6):  
    
    for j in range(1, k + 1):
        print(' ', end='')
    k -= 2  

    num = i
    for j in range(1, i):
        print(num, end=' ')
        num += 1

    for j in range(i):
        print(num, end=' ')
        num -= 1

    print()
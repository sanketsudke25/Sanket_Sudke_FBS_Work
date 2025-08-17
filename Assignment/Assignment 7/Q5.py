for i in range(1, 6):  
    
    for j in range(5 - i):
        print(' ', end='')

    if (i == 1):
        print('1')
    elif (i == 5):
        for j in range(1, 6):
            print(j, end=' ')
        print()
    else:
        print('1', end='')
        for j in range(2 * i - 3):
            print(' ', end='')
        print('1')

                                    
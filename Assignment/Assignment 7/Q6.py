for i in range(1, 6):
    if (i == 1):
        for j in range(1, 6):
            print(j, end=' ')
        print()
    else:
        
        for j in range(i - 1):
            print('', end='')

        print(i, end=' ')

      
        for j in range(2 * (5 - i) - 1):
            print('', end=' ')

        if (i != 5):
            print('5')
        else:
            print()

          
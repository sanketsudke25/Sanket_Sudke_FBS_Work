for i in range(1, 6):
    for j in range(1, 6):
        if(i+j%2==0):
          print('',end =  '')
    for j in range(j , i+6):
        print('1',end='') 
    for j in range(j , 7-i):
        print('0',end='')  
    print() 

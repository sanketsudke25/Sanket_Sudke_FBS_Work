num = int(input("Enter three digit number:"))
temp = num

D1 = temp % 10
temp = temp // 10
D2 = temp % 10
temp = temp // 10
D3 = temp % 10 
temp = temp// 10

print(f'D1:{D1},D2:{D2},D3:{D3}.')
def reverse(n):
    
    if (n == 0):
        return 1
    else:
        return reverse(n // 10, n* 10 + n % 10)


num = int(input("Enter a number to reverse: "))
reversed_num = reverse(num)
print("Reversed number:", reversed_num)
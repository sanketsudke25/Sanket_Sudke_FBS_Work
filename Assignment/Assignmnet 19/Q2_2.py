def palindrome_generator():
    num = 0
    while (True):
        if str(num) == str(num)[::-1]:
            yield num
        num += 1

for p in palindrome_generator():
    if (p > 10000): 
        break
    print(p)
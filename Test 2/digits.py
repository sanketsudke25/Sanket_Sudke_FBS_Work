num = int(input("Enter the three digits number:"))
if(num<100 or num>999):
    print("please enter the vaild three digits number")
else:
      first  = num//100
      second = (num//100)%10
      third  = num%10
if(first == 2 * second  and frist  ==third /2):
    print(Yes, "you have done it")
else:
        print("Please try next time")
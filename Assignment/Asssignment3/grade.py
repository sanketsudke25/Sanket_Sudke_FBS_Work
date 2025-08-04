m1 = int(input("Enter marks of subject 1:"))
m2 = int(input("Enter marks of subject 2:"))
m3 = int(input("Enter marks of subject 3:"))
m4 = int(input("Enter marks of subject 4:"))
m5 = int(input("Enter marks of subject 5:"))

avg = (m1 + m2 + m3 + m4 + m5) / 5
gain_marks =m1 + m2 + m3 + m4 +m5 
percentage = (gain_marks/500)*100

if(avg > 90):
    print('Frist class')
elif(avg > 85):
    print('second class')
elif(avg > 65):
        print('pass')
else:
        print('fail')       
print(f'percentage is {percentage} %')
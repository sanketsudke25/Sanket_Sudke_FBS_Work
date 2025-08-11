
num = int(input("Enter number of students: "))

total_percentage = 0

for i in range(num):
    print("Enter marks for 5 subjects:")
    total = 0

    for j in range(5):
        marks = float(input("Enter marks: "))
        total += marks

    percentage = (total / 500) * 100
    print("Percentage:", percentage)
    total_percentage += percentage

average = total_percentage / num
print("Average Percentage of all students:", average)
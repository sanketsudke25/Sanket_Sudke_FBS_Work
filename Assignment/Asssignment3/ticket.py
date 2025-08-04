age1 = int(input("Enter age of person 1: "))
age2 = int(input("Enter age of person 2: "))
age3 = int(input("Enter age of person 3: "))
age4 = int(input("Enter age of person 4: "))
age5 = int(input("Enter age of person 5: "))
ticket_amt = int(input("Enter ticket amount: "))

# Person one
if age1 < 12:
    dis_amt = ticket_amt * 0.3  # 30% discount
    amt1 = ticket_amt - dis_amt
elif age1 > 59:
    dis_amt = ticket_amt * 0.5  # 50% discount
    amt1 = ticket_amt - dis_amt
else:
    amt1 = ticket_amt

# Person two
if age2 < 12:
    dis_amt = ticket_amt * 0.3  # 30% discount
    amt2 = ticket_amt - dis_amt
elif age2 > 59:
    dis_amt = ticket_amt * 0.5  # 50% discount
    amt2 = ticket_amt - dis_amt
else:
    amt2 = ticket_amt

# Person three
if age3 < 12:
    dis_amt = ticket_amt * 0.3
    amt3 = ticket_amt - dis_amt
elif age3 > 59:
    dis_amt = ticket_amt * 0.5
    amt3 = ticket_amt - dis_amt
else:
    amt3 = ticket_amt

#Person four
if age4 < 12:
    dis_amt = ticket_amt * 0.3
    amt4 = ticket_amt - dis_amt
elif age4  > 59:
    dis_amt = ticket_amt * 0.5
    amt4 = ticket_amt - dis_amt
else:
    amt4 = ticket_amt

#Person fifth
if age5 < 12:
    dis_amt = ticket_amt * 0.3
    amt5 = ticket_amt - dis_amt
elif age5 > 59:
    dis_amt = ticket_amt * 0.5
    amt5 = ticket_amt - dis_amt
else:
    amt5 = ticket_amt

# Total amount
total_amt = amt1 + amt2 + amt3 + amt4 + amt5
print("Total amount to be paid:", total_amt)

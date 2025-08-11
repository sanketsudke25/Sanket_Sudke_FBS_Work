amt = int(input("Enter amount to calculate min no. of notes: "))
temp = amt
total_notes = 0

denominations = [2000, 500, 200, 100, 50, 20, 10]

for i in range(len(denominations)):
    note = denominations[i]
    total_notes += temp // note
    temp = temp % note

print("Min no. of notes:", total_notes)
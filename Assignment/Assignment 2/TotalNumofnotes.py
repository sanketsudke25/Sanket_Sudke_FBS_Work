amt = int(input("Enter amount to calculate min no.of notes:"))
temp = amt
two_thousand = temp // 2000
temp = temp % 2000

five_hundered = temp //500
temp = temp %500

two_hundered = temp//200
temp =temp%200

hundered = temp//100
temp =temp%100

fifty = temp // 50
temp = temp %50

twenty = temp // 20
temp = temp % 20

Ten = temp // 10
temp = temp % 10

total_notes = two_thousand + five_hundered + two_hundered + hundered + fifty + twenty + Ten

print(f'min no.of notes {total_notes}')

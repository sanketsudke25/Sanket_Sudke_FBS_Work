amt = int(input("Enter amount to calculate min no.of notes: "))
temp = amt
denominations = [2000, 500, 200, 100, 50, 20, 10,5]
note_counts = []
for denom in denominations:
    count = temp // denom
    temp = temp % denom
    note_counts.append((denom, count))
total_notes = sum(count for _, count in note_counts)

print(f"Minimum number of notes: {total_notes}")
print("close:")
for denom, count in note_counts:
    if (count > 0):
        print(f"{denom} , {count}")

original = "sanket"
if len(original) < 2:
    new_string = original 
else:
    chars = []
    for ch in original:
        chars.append(ch)

  
    temp = chars[0]
    chars[0] = chars[len(chars) - 1]
    chars[len(chars) - 1] = temp

    new_string = ""
    for ch in chars:
        new_string += ch

print("Original String:", original)
print("Modified String:", new_string)
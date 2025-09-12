words = ["flower", "flow", "flight"]
min_length = min(len(word) for word in words)
prefix = ""
for i in range(min_length):
    char_set = set(word[i] for word in words)
    
    if len(char_set) == 1:
        prefix += char_set.pop()
    else:
        break  
    print("Longest Common Prefix:", prefix)
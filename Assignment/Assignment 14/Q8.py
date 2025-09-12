words = ["listen", "silent", "enlist", "rat", "tar", "art", "evil", "vile", "live"]

anagram_groups = {}

for word in words:
    signature = ''.join(sorted(word))
    
    if signature in anagram_groups:
        anagram_groups[signature].append(word)
    else:
        anagram_groups[signature] = [word]
print("Grouped Anagrams:")
for group in anagram_groups.values():
    print(group)
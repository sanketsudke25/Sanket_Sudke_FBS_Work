set1 = {1, 2, 3, 4, 5, 6}
set2 = {4, 5, 6, 7, 8}
missing_in_set2 = set1 - set2
missing_in_set1 = set2 - set1
print("Elements in set1 but missing in set2:", missing_in_set2)
print("Elements in set2 but missing in set1:", missing_in_set1)
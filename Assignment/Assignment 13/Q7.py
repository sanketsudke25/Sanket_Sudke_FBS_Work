my_dict = {'name': 'Sanket', 'age': 22, 'location': 'pusad'}
key_to_remove = 'age'

if key_to_remove in my_dict:
    del my_dict[key_to_remove]
    print(f"Key '{key_to_remove}' removed successfully.")
else:
    print(f"Key '{key_to_remove}' not found in the dictionary.")
print("Updated Dictionary:", my_dict)
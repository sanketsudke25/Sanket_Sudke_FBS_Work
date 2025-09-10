
input_string = input("Enter a string: ")


modified_string = ""


for i in range(len(input_string)):
    if input_string[i] == ' ':
        modified_string += '-'  
    else:
        modified_string += input_string[i]  


print("Modified String:", modified_string)
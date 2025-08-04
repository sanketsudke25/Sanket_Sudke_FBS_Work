
seconds = float(input("Enter seconds :"))

hours = seconds // 3600
minutes = seconds //60
seconds = seconds % 60

print(f'{hours} hours, {minutes} minutes,{seconds} seconds')

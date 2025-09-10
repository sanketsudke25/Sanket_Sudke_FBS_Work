li = [10, 20, 30, 50, 100]

max = li[0]
smax = li[0]

for i in range(1, len(li)):
    if(li[i] > max):
        smax = max
        max = li[i]
    elif(li[i] > smax):
        smax = li[i]

print("Second max is", smax)
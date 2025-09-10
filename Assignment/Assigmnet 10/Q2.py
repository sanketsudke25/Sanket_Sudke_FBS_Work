li = [10,30,50,20,40,80] 
max=li[0]
min=li[0] 
for i in range(1,len(li)):
     if(li[i]>max):
        max=li[i]
     if(li[i]<min):  
        min=li[i] 
print("maxi number is ",max)    
print("min number is ",min)        




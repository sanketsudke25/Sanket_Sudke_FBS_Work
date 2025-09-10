coins = [2, 7, 2, 4, 7]  

for i in coins:
    count = coins.count(coin) 
    if (count % 2 != 0):        
        print("Missing coin:", coin)
        break
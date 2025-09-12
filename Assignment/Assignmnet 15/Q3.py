class Shirt:
    def __init__(self,pid,name,price,quantity): 
        self.p = pid
        self.nm = name
        self.p = price
        self.q = quantity
    def showShirt(self):
        print("pid:",self.p)
        print("name:",self.nm)
        print("price:",self.p)
        print("quantity",self.q)
    def __del__(self):  
        print(f"product quantity is {self.q} record deleted.")
p1 = Shirt(101,"MK",500,"boring")   
p1.showShirt()
print("created the Shirt system")
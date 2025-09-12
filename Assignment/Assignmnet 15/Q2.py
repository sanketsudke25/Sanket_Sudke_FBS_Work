class Product:
    def __init__(self,pid,name,price,quantity): 
        self.p = pid
        self.nm = name
        self.p = price
        self.q = quantity
    def showProduct(self):
        print("pid:",self.p)
        print("name:",self.nm)
        print("price:",self.p)
        print("quantity",self.q)
    def __del__(self):  
        print(f"product {self.q} record deleted.")
p1 = Product(101,"phone",1500,"A1")   
p1.showProduct()
print("created the Product")
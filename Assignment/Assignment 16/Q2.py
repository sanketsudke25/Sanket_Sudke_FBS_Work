class Product:
    
    discount = 0.1   

    def __init__(self, pid, pname, price, quantity):
        self.pid = pid
        self.pname = pname
        self.price = price
        self.quantity = quantity


    def __del__(self):

        print("Destructor called for:", self.pname)


    def showProduct(self):
        print("Product ID:", self.pid)
        print("Product Name:", self.pname)
        print("Price:", self.price)
        print("Quantity:", self.quantity)


    def applyDiscount(self):
        discounted_price = self.price - (self.price * Product.discount)
        print("Price after discount:", discounted_price)



p1 = Product(101,"mobile",4500,3)   
p1.showProduct()
p1.applyDiscount()

p2 = Product(201, "Laptop", 50000, 2)   
p2.showProduct()
p2.applyDiscount()
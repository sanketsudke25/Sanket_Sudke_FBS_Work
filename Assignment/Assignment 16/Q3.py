class Shirt:
    count = 0   

    def __init__(self, sid, sname, price, type, size):
        self.sid = sid
        self.sname = sname
        self.price = price
        self.type = type
        self.size = size
        Shirt.count += 1

    def __del__(self):
        print("Destructor called for:", self.sname)
        Shirt.count -= 1

    def showBook(self):
        multipliers = {'small': 1.0, 'medium': 1.1,'large': 1.2,'xlarge': 1.3 }
        multiplier = multipliers.get(self.size.lower(), 1.0)
        final_price = self.price * multiplier
        print("Shirt ID:", self.sid)
        print("Shirt Name:", self.sname)
        print("Type:", self.type)
        print("Size:", self.size)
        print("Final Price :",format(final_price))

    @staticmethod
    def showCount():
        print("Total Shirts:", Shirt.count)

s1 = Shirt(12, "Formal White", 1000, "Formal", "small")
s1.showBook()
s2 = Shirt(101, "Casual Blue", 1000, "Casual", "large")
s2.showBook()

Shirt.showCount()
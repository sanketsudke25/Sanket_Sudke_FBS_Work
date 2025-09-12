class Book:
    def __init__(self,bid,name,price,author): 
        self.b = bid
        self.nm = name
        self.p = price
        self.a = author
    def showBook(self):
        print("bid:",self.b)
        print("name:",self.nm)
        print("price:",self.p)
        print("author",self.a)
    def __del__(self):  
        print(f"book {self.nm} record deleted.")
b1 = Book(101,"python programming",200,"sanket")   
b1.showBook()
print("created the book")
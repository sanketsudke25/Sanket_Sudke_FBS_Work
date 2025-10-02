class Book:
    count = 0

  
    def __init__(self, bid, bname, price, author):
        self.bid = bid
        self.bname = bname
        self.price = price
        self.author = author
        Book.count += 1   

    def __del__(self):

        print("Destructor called for:", self.bname)
        Book.count -= 1  


    def showBook(self):
        print("Book ID:", self.bid)
        print("Book Name:", self.bname)
        print("Price:", self.price)
        print("Author:", self.author)

    
    @staticmethod
    def showCount():
        print("Total Books:", Book.count)



b1 = Book(12," how to stop overthinking",200,"om")   
b1.showBook()

b2 = Book(101, "Python", 500, "Sanket")  
b2.showBook()

Book.showCount()
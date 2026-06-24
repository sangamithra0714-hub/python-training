class library:
    def __init__(self,name,author,publisher):
        self.name=name
        self.author=author
        self.publisher=publisher
    def persondetails(self,phonenumber):
        self.phonenumber=phonenumber
        print("phone num is :",self.phonenumber)
    def display(self):
        print("Book Name:", self.name)
        print("Author:", self.author)
        print("Publisher:", self.publisher)
p1=library("python","Mithra","Ravi")
p1.persondetails(123456789)
p1.display()

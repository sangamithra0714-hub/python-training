class Book:
    def details(self,title,author):
        self.title=title
        self.author=author
    def display(self):
        print("title of the book is",self.title)
        print("author of the book is",self.author)
s=Book()
s.details("python programming","Abdul")
s.display()

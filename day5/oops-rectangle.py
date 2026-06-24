class rectangle:
    def __init__ (self,length,breadth):
        self.length=length
        self.breadth=breadth
    def area(self):
        print("the area of the rectangle is:",self.length*self.breadth)
s=rectangle(23,34)
s.area()

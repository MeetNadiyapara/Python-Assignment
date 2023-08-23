'''Write a Python class named Rectangle constructed by a length and
width and a method which will compute the area of a rectangle'''
class rectangle:
    def inp(self):
        self.len=int(input("Enter Length: "))
        self.wid=int(input("Enter Width: "))
    def out(self):
        self.mul=(self.len*self.wid)
        print("Area of rectangle: ",self.mul)
    
obj=rectangle()
obj.inp()
obj.out()
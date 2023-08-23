'''Write a Python class named Circle constructed by a radius and two
methods which will compute the area and the perimeter of a circle'''

class circle:
    pi=3.14
    #rad=0
    def inp(self):
        self.rad=int(input("Enter Radius: "))
    def area(self):
        print("area of circle is: ",self.pi*self.rad**2)
    def perimeter(self):
        print("perimeter of circle is: ",self.pi*2*self.rad)

obj=circle()
obj.inp()
obj.area()
obj.perimeter()
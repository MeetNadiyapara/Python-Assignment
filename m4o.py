class Vehicle:

    def inp(self):
        self.name=input("Enter Name: ")
        self.max_speed=input("Enter Speed: ")
        self.mileage=input("Enter Milage: ")


    
    def inp1(self):
        self.name1=input("Enter Name: ")
        self.max_speed1=input("Enter Speed: ")
        self.mileage1=input("Enter Milage: ")

class bus(Vehicle):
    pass
class car(bus):
    
    def inp12(self):
        print("Mileage:",self.mileage,"Speed: ",self.max_speed,"name:",self.name)
    
    def inp123(self):

        print("Mileage:",self.mileage1,"Speed: ",self.max_speed1,"name:",self.name1)

obj=car()
obj.inp()
obj.inp1()
obj.inp12()
obj.inp123()

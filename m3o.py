#Create a child class Bus that will inherit all of the variables and methods of the Vehicle class
class vehicle:
    def se(self):
        self.money=input("Enter Money: ")
        self.car=input("Enter Cars: ")
    def se1(self):
        print("This Is vehicle car: ",self.car)
        print("This Is vehicle money: ",self.money)

class child(vehicle):
    def se2(self):
        print("This Is vehicle  Child car: ",self.car)
        print("This Is vehicle child money: ",self.money)

obj=child()
obj.se()
obj.se1()
obj.se2()
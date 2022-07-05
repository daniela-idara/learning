#
# Example file for working with classes
# LinkedIn Learning Python course by Joe Marini
#

class Vehicle():
    def __init__(self, bodystyle):
        self.bodystyle = bodystyle
    
    def drive(self,speed):
        self.mode = "driving"
        self.speed = speed

class Car(Vehicle):
    def __init__(self, enginetype):
        super().__init__("Car")
        self.wheels = 4
        self.doors = 4
        self.enginetype = enginetype

    def drive(self, speed):
        super().drive(speed)
        print("Driving my", self.enginetype, "car at", self.speed, "mph")

class Motorcyle(Vehicle):
    def __init__(self, enginetype, hassidecar):
        super().__init__("Motorcyle")
        if (hassidecar):
            self.wheels = 3
        else:
            self.wheels = 2
        self.doors = 0
        self.enginetype = enginetype
    
    def drive(self, speed):
        super().drive(speed)
        print("Driving my", self.enginetype, "motorcycle at", self.speed, "mph")

car1 = Car("gas")
car2 = Car("electric")
mc1 = Motorcyle("gas", True)
car1.drive(30)
car2.drive(40)
mc1.drive(50)

print(mc1.wheels)
print(car1.enginetype)
print(car2.doors)
print(car2.enginetype)

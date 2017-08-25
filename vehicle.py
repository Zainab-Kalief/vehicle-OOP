class Vehicle(object):
    def __init__(self, wheels, capacity, make, model):
        self.wheels = wheels
        self.capacity = capacity
        self.make = make
        self.model = model
        self.mileage = 0 #we dont set parameters for defaults
    def drive(self, miles):
        self.miles += miles
        return self
    def reverse(self,miles):
        self.miles -= miles
        return self

#implicit inheritance 
class Bike(Vehicle):
    #we have no init set cos it has no extra init
    def vehicleType(self):
        return 'Bike'

class Car(Vehicle):
    def setWheels(self):
        self.wheels = 4
        return self

class Airplane(Vehicle):
    def fly(self,miles):
        self.mileage += miles
        return self


tomCar = Vehicle(4,8,'Chevi','minivan')
print tomCar.make

rider = Bike(2,1,'Pimping','Paramount')

airFly = Airplane(22,800,'Airbus','A300')
airFly.fly(500)
print airFly.mileage

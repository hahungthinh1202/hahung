

class Car:
    curSpeed = 0
    TravelledDistance = 0

    def __init__(self, RegNumber, MaxSpeed):
        self.RegNumber = RegNumber
        self.MaxSpeed = MaxSpeed

    def Accelerate(self, acceleration):
        self.curSpeed += acceleration
        if self.curSpeed > self.MaxSpeed:
            self.curSpeed = self.MaxSpeed
        elif self.curSpeed < 0:
            self.curSpeed = 0

    def Drive(self, hours):
        self.TravelledDistance = self.TravelledDistance + self.curSpeed * hours

class ElectricCar(Car):
    def __init__(self, regNumber, maxSpeed, batteryCapacity):
        Car.__init__(self, regNumber, maxSpeed)
        self.BatteryCapacity = batteryCapacity

class GasolineCar(Car):
    def __init__(self, regNumber, maxSpeed, tankVollume):
        Car.__init__(self, regNumber, maxSpeed)
        self.TankVollume = tankVollume

#main

print("Create new car")
MyCarList = [ElectricCar("ABC-15", 180, 52.5),
             GasolineCar("ACD-123", 165, 32.3)]
for i in range (3):
    MyCarList[0].Accelerate(120)
    MyCarList[1].Accelerate(115)
    MyCarList[0].Drive(1)
    MyCarList[1].Drive(1)

print(MyCarList[0].RegNumber,"has travelled",MyCarList[0].TravelledDistance, "km")
print(MyCarList[1].RegNumber,"has travelled",MyCarList[1].TravelledDistance, "km")





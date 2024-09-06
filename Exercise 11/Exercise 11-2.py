from prettytable import PrettyTable

class Car:
    CurSpeed = 0
    TravelledDistance = 0

    def __init__(self, RegNumber, MaxSpeed):
        self.RegNumber = RegNumber
        self.MaxSpeed = MaxSpeed

    def Accelerate(self, Acceleration):
        self.CurSpeed += Acceleration
        if self.CurSpeed > self.MaxSpeed:
            self.CurSpeed = self.MaxSpeed
        elif self.CurSpeed < 0:
            self.CurSpeed = 0

    def Drive(self, Hours):
        self.TravelledDistance = self.TravelledDistance + self.CurSpeed * Hours

class ElectricCar(Car):
    def __init__(self, RegNumber, MaxSpeed, BatteryCapacity):
        Car.__init__(self, RegNumber, MaxSpeed)
        self.BatteryCapacity = BatteryCapacity

class GasolineCar(Car):
    def __init__(self, RegNumber, MaxSpeed, TankVollume):
        Car.__init__(self, RegNumber, MaxSpeed)
        self.TankVollume = TankVollume

#main
print("Create new car")

MyCarList = [ElectricCar("ABC-15", 180, 52.5),
             GasolineCar("ACD-123", 165, 32.3)]
for i in range (3):
    MyCarList[0].Accelerate(120)
    MyCarList[1].Accelerate(115)
    MyCarList[0].Drive(1)
    MyCarList[1].Drive(1)

print(MyCarList[0].TravelledDistance)
print(MyCarList[1].TravelledDistance)





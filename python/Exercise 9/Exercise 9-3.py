class Car:
    current_speed = 0
    travelled_distance = 0

    def __init__(self, registration_number, maximum_speed):
        self.registration_number = registration_number
        self.maximum_speed = maximum_speed

    def accelerate(self, acceleration):
        self.current_speed += acceleration
        if self.current_speed > self.maximum_speed:
            self.current_speed = self.maximum_speed
        elif self.current_speed < 0:
            self.current_speed = 0

    def drive(self, hours):
        self.travelled_distance = self.travelled_distance + self.current_speed * hours

#main
reg_num = "BRK-782"     #input("Enter your registration number: ")
max_speed = 120         #input("Enter maximum speed: ")

car = Car(reg_num, max_speed)

print(f"Information of the car is:\nCar registation {car.registration_number}\nMaximum speed {car.maximum_speed}"
      f"\nCurrent speed {car.current_speed}"
      f"\nTravelled distance {car.travelled_distance}\n")
print(f"Acceleration... Current speed {car.current_speed}. Travelled distance {car.travelled_distance}")
car.accelerate(30)
car.drive(1.5)
print(f"Acceleration... Current speed {car.current_speed}. Travelled distance {car.travelled_distance}")
car.accelerate(70)
car.drive(2)
print(f"Acceleration... Current speed {car.current_speed}. Travelled distance {car.travelled_distance}")
car.accelerate(50)
car.drive(0.75)
print(f"Acceleration... Current speed {car.current_speed}. Travelled distance {car.travelled_distance}")
car.accelerate(-200)
car.drive(1)
print(f"Emergency brake... Current speed {car.current_speed}. Travelled distance {car.travelled_distance}")





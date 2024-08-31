from random import randint
from prettytable import PrettyTable


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

class race:
    def __init__(self, name, distance, car):
        self.car = car
        self.name = name
        self.distance = distance

    def hour_passes(self):
        for i in range(len(self.car)):
            self.car[i].accelerate(randint(-10, 15))
            self.car[i].drive(1)

    def print_status(self):
        table = PrettyTable()
        table.field_names = ["Car register number", "Current speed", "Travelled distance"]
        for i in range(len(self.car)):
            table.add_row([self.car[i].registration_number, self.car[i].current_speed, self.car[i].travelled_distance])
        print(table)

    def race_finished(self):
        for i in range(len(self.car)):
            if self.car[i].travelled_distance >= self.distance:
                return True
        return False

#main
car_list = []
for i in range(0, 10):
    car_list.append(Car("BRK-78" + str(i), randint(100, 200)))
    print(
        f"Information of the car is:\nCar registation {car_list[i].registration_number}\nMaximum speed {car_list[i].maximum_speed}"
        f"\nCurrent speed {car_list[i].current_speed}"
        f"\nTravelled distance {car_list[i].travelled_distance}\n")

my_race = race("Grand Demolition Derby", 8000, car_list)
hour_pass    = 0
while not my_race.race_finished():
    my_race.hour_passes()
    hour_pass += 1
    if hour_pass % 10 == 0:
        print(f"Standing after {hour_pass} hours:")
        my_race.print_status()

print(f"Race finished after {hour_pass} hours, final standing:")
my_race.print_status()

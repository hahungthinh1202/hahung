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

class Race:
    winning_car = None
    def __init__(self, name, distance, car):
        self.car = car
        self.name = name
        self.distance = distance


    def hour_passes(self):
        for car in self.car:
            car.accelerate(randint(-10, 15))
            car.drive(1)

    def print_status(self):
        table = PrettyTable()
        table.field_names = ["Car register number", "Current speed", "Travelled distance"]
        for car in self.car:
            table.add_row([car.registration_number, car.current_speed, car.travelled_distance])
        print(table)

    def race_finished(self):
        for car in self.car:
            if car.travelled_distance >= self.distance:
                self.winning_car = car.registration_number
                return True
        return False

#main
car_list = []
print("Creating car list....")
car_list_table = PrettyTable()
car_list_table.field_names = (["Car register number","Maximum speed"])
for i in range(0, 10):
    speed = randint(100, 200)
    car_list.append(Car("BRK-78" + str(i),speed))
    car_list_table.add_row(["BRK-78" + str(i), speed])

print(car_list_table)

my_race = Race("Grand Demolition Derby", 8000, car_list)

print(f"\n\n{my_race.name} starts....")
hour_pass    = 0
while not my_race.race_finished():
    my_race.hour_passes()
    hour_pass += 1
    if hour_pass % 10 == 0:
        print(f"\nStanding after {hour_pass} hours:")
        my_race.print_status()

print(f"Race finished after {hour_pass} hours, final standing:")
my_race.print_status()
print(f"The winning car is {my_race.winning_car}")

from random import randint
class car:
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
car_list = []
for i in range(0,10):
    car_list.append( car("BRK-78"+str(i), randint(100,200)))
    print(f"Information of the car is:\nCar registation {car_list[i].registration_number}\nMaximum speed {car_list[i].maximum_speed}"
          f"\nCurrent speed {car_list[i].current_speed}"
          f"\nTravelled distance {car_list[i].travelled_distance}\n")


finish_flag = -1
hour = 1
print(f"Hour\t{car_list[0].registration_number:8}{car_list[1].registration_number:8}{car_list[2].registration_number:8}"\
      f"{car_list[3].registration_number:8}{car_list[4].registration_number:8}{car_list[5].registration_number:8}"
      f"{car_list[6].registration_number:8}{car_list[7].registration_number:8}{car_list[8].registration_number:8}{car_list[9].registration_number:8}")
while finish_flag != -1:
    for i in range(0,10):
        car_list[i].accelerate(randint(-10,15))
        car_list[i].drive(1)
    for i in range(0,10):
        if car_list[i].travelled_distance >= 10000:
            finish_flag = i
    hour += 1
    print(f"{hour:2}  {car_list[0].travelled_distance:8.2f} {car_list[1].travelled_distance:8.2f} {car_list[2].travelled_distance:8.2f}"
          f"{car_list[3].travelled_distance:8.2f} {car_list[4].travelled_distance:8.2f} {car_list[5].travelled_distance:8.2f}"
          f"{car_list[6].travelled_distance:8.2f} {car_list[7].travelled_distance:8.2f} {car_list[8].travelled_distance:8.2f}"
          f"{car_list[9].travelled_distance:8.2f}")
print(f"The winning car is {car_list[finish_flag].registration_number}")

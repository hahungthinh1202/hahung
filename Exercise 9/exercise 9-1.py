class car:
    current_speed = 0
    travelled_distance = 0
    def __init__(self, registration_number, maximum_speed):
        self.registration_number = registration_number
        self.maximum_speed = maximum_speed

#main
reg_num = input("Enter your registration number: ")
max_speed = input("Enter maximum speed: ")

car_data = car(reg_num, max_speed)

print(f"Information of the car is:\nCar registation {car_data.registration_number}\nMaximum speed {car_data.maximum_speed}"
      f"\nCurrent speed {car_data.current_speed}"
      f"\nTravelled distance {car_data.travelled_distance}")
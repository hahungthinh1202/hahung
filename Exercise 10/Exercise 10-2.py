class elevator:
    def __init__(self, bottom_floor, top_floor):
        self.bottom_floor = bottom_floor
        self.top_floor = top_floor
        self.current_floor = bottom_floor

    def go_to_floor(self, floor):
        if floor < self.bottom_floor or floor > self.top_floor:
            print("error")
        elif floor < self.current_floor:
            for i in range (1, self.current_floor-floor+1):
                self.floor_down()
                print(f"going down currently {self.current_floor}")

        elif floor > self.current_floor:
            for i in range (1, floor-self.current_floor+1):
                self.floor_up()
                print(f"going up currently {self.current_floor}")

    def floor_up(self):
        self.current_floor += 1

    def floor_down(self):
        self.current_floor -= 1

class building:
    def __init__(self, bottom_floor, top_floor, elevator_count):
        self.bottom_floor = bottom_floor
        self.top_floor = top_floor
        self.elevator_list = []
        for i in range(elevator_count):
            self.elevator_list.append(elevator(self.bottom_floor, self.top_floor))

    def run_elevator(self,elevator_number, goto_floor ):
        self.elevator_list[elevator_number-1].go_to_floor(goto_floor)

#main
print("Create new building....")
top_floor = int(input("Enter your top floor: "))
elevator_count = int(input("Enter number of elevators: "))
my_building = building(1, top_floor, elevator_count)
print("Using elevator")
print(f"There are {elevator_count} elevators in your building")
while True:
    current_elevator = int(input("Enter elevator number you want to use: "))
    to_floor = input(f"Current floor of elevator {current_elevator} "
                     f"is {my_building.elevator_list[current_elevator-1].current_floor}. "
                     f"Enter floor you want to go (empty string to exit): ")
    if to_floor == "":
        print(f"Go back to bottom floor")
        my_building.elevator_list[current_elevator-1].go_to_floor(1)
        break
    else:
        my_building.elevator_list[current_elevator-1].go_to_floor(int(to_floor))





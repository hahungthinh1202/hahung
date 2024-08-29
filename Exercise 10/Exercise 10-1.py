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

#main
print("Create new elevator....")
top_floor = int(input("Enter your top floor: "))
my_elevator = elevator(1, top_floor)

print("Using elevator....")
while True:
    to_floor = input(f"Current floor is {my_elevator.current_floor}. Enter floor you want to go(empty string to exit): ")
    if to_floor == "":
        print(f"Go back to bottom floor")
        my_elevator.go_to_floor(my_elevator.bottom_floor)
        break
    else:
        my_elevator.go_to_floor(int(to_floor))





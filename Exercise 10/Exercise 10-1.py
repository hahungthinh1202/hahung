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

my_elevator = elevator(1, 10)
my_elevator.go_to_floor(5)
print(my_elevator.current_floor)

my_elevator.go_to_floor(7)
print(my_elevator.current_floor)

my_elevator.go_to_floor(my_elevator.bottom_floor)
print(my_elevator.current_floor)



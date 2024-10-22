class visitor:
    def __init__(self, name, height):
        self.name = name
        self.height = height


class attraction:
    def __init__(self,name, height_limit):
        self.all_visitor = []
        self.name = name
        self.height_limit = height_limit

    def new_visitor(self, name, height):
        if height >= self.height_limit:
            print(f"{name} is allowed!")
            self.all_visitor.append(visitor(name, height))
        else:
            print(f"{name} is too short!")
    def check_height(self, visitor_name):
        if visitor_name in self.all_visitor:
            if visitor_name.height == self.height_limit:
                pass

    def show_all_visitor(self):
        for visitor in self.all_visitor:
            print(visitor.name)

#main
my_park = attraction("new_helsinki", 160)
my_park.new_visitor("mr A", 160)
my_park.new_visitor("mrs B",155)
my_park.new_visitor("mr C", 160)
my_park.new_visitor("mr D",175)
my_park.new_visitor("mrs E", 190)
my_park.new_visitor("mr F",162)

my_park.show_all_visitor()

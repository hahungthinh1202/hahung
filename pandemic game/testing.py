
from prettytable import PrettyTable

table  = PrettyTable()

car_list = ["a",'b','c','d','e','f','g','h','i','j']
table.field_names = car_list
table.add_row(car_list)
print(table)
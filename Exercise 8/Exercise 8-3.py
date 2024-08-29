import mysql.connector as mysql
from geopy import distance as distance_calculator
from geopy.distance import distance

#main
connection = mysql.connect(
    host='localhost',
    user='root',
    passwd='1202',
    database='flight_game'
)

cursor = connection.cursor()
ICAO_code1 = input("please enter the first ICAO: ")
ICAO_code2 = input("please enter the second ICAO: ")
command = f"select name, latitude_deg, longitude_deg from airport where ident = '{ICAO_code1}';"
cursor.execute(command)
location1 = cursor.fetchall()
command = f"select name, latitude_deg, longitude_deg from airport where ident = '{ICAO_code2}';"
cursor.execute(command)
location2 = cursor.fetchall()
result = distance_calculator.distance(location1[0][1:3], location2[0][1:3])

print(f"The distance between {location1[0][0]} and {location2[0][0]} is {result}")


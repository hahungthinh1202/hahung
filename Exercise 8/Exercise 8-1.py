import mysql.connector as mysql
import requests
import json

#main
connection = mysql.connect(
    host='localhost',
    user='root',
    passwd='1202',
    database='flight_game'
)
cursor = connection.cursor()
ICAO_code = input("Please enter your ICAO code: ")
command = f"select name, municipality from airport where ident = '{ICAO_code}';"
cursor.execute(command)
data =cursor.fetchall()
print(f"the airport with {ICAO_code} code is {data[0][0]} and located in {data[0][1]}")



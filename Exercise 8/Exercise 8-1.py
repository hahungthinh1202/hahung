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
ICAO_code = "00GA"
command = f"select latitude_deg, longitude_deg from airport where ident = '{ICAO_code}';"
cursor.execute(command)
data =cursor.fetchall()
print(data[0][0])



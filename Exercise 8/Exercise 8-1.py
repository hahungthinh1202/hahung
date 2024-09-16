import mysql.connector
import requests
import json

#main
connection = mysql.connector.connect(
    host='localhost',
    user='root',
    passwd='1202',
    database='flight_game'
)

ICAO_code = input("Please enter your ICAO code: ")

cursor = connection.cursor()
cursor.execute( f"select name, municipality from airport where ident = '{ICAO_code}';")
data =cursor.fetchall()


print(f"the airport with {ICAO_code} code is {data[0][0]} and located in {data[0][1]}")



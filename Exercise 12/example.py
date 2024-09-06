import requests
import mysql.connector as mysql

connection = mysql.connect(
    host='localhost',
    user='root',
    passwd='1202',
    database='flight_game'
)
cursor = connection.cursor()
command = f"select name, municipality from airport where ident = '{ICAO_code}';"

x = requests.get('https://w3schools.com/python/demopage.htm')



print(x.text)
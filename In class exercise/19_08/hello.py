import mysql.connector as mysql

#main
connection = mysql.connect(
    host='localhost',
    user='root',
    passwd='1202',
    database='flight_game'
)
cursor = connection.cursor()
ICAO_code = input("please enter the ICAO  code: ")
command = f"select name, municipality from airport where ident = '{ICAO_code}';"
cursor.execute(command)
data = cursor.fetchall()
print(f"The ICAO code {ICAO_code} is belong to {data[0][0]} in {data[0][1]} city")

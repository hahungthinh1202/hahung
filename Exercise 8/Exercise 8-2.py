import mysql.connector as mysql

#main
connection = mysql.connect(
    host='localhost',
    user='root',
    passwd='1202',
    database='flight_game'
)

cursor = connection.cursor()
area_code = input("please enter the area code (example FI for Finland): ")
command = f"select name, type from airport where iso_country = '{area_code}' order by airport.type DESC;';"
cursor.execute(command)
data = cursor.fetchall()
print("the list of airport below")
for row in data:
    print(f"\t{row[0]:35} {row[1]} ")
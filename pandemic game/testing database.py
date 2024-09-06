import mysql.connector as mysql
import hello
from database_interaction import *
connection = mysql.connect(
    host='localhost',
    user='root',
    passwd='1202',
    database='flight_game'
)

test_db()

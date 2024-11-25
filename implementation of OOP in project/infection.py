import mysql.connector
import random

import SQL


class Infection:

    def __init__(self):
        pass

    def Reset_deck(self):
        SQL.update("delete from infection_deck;")
        order = list(range(1, 49))
        random.shuffle(order)
        for i in order:
            SQL.update(f"insert into infection_deck values ({i});")


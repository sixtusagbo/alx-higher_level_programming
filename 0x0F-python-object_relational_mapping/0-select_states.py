#!/usr/bin/python3
"""
Lists all states from the database hbtn_0e_0_usa
Takes 3 arguments: mysql username, mysql password and database name
"""
import MySQLdb
from sys import argv

if __name__ == '__main__':
    # Connect to db
    db = MySQLdb.connect(user=argv[1], passwd=argv[2], db=argv[3], port=3306)

    # Grab the cursor
    cur = db.cursor()
    cur.execute("SELECT * FROM states AS s ORDER BY s.id;")
    states = cur.fetchall()

    for state in states:
        print(state)

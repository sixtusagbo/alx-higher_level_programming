#!/usr/bin/python3
"""
Lists all cities from the database hbtn_0e_4_usa
"""
import MySQLdb
from sys import argv

if __name__ == '__main__':
    # Connect to db
    conn = MySQLdb.connect(host="localhost", user=argv[1], passwd=argv[2],
                           db=argv[3], port=3306, charset="utf8")

    # Grab the cursor
    cur = conn.cursor()
    cur.execute("SELECT cities.id, cities.name, states.name FROM cities JOIN "
                "states ON cities.state_id = states.id")
    query_rows = cur.fetchall()

    for row in query_rows:
        print(row)

    cur.close()
    conn.close()

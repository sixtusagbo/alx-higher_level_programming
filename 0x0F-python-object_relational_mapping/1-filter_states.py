#!/usr/bin/python3
"""
Lists all states with a name starting with N (upper N)
Takes 3 arguments: mysql username, mysql password and database name
"""
import MySQLdb
from sys import argv

if __name__ == '__main__':
    # Connect to db
    conn = MySQLdb.connect(host=localhost, user=argv[1], passwd=argv[2], db=argv[3], port=3306)

    # Grab the cursor
    cur = conn.cursor()
    cur.execute("SELECT * FROM states AS s ORDER BY s.id")
    states = cur.fetchall()

    for state in states:
        if row[1].startswith('N'):
            print(state)

    cur.close()
    conn.close()

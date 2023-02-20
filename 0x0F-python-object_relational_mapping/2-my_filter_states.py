#!/usr/bin/python3
"""
Takes in an argument and displays all values in the
states table of hbtn_0e_0_usa where name matches the argument.
"""
import MySQLdb
from sys import argv

if __name__ == '__main__':
    # Connect to db
    conn = MySQLdb.connect(host="localhost", user=argv[1], passwd=argv[2],
                           db=argv[3], port=3306)

    # Grab the cursor
    cur = conn.cursor()
    cur.execute("SELECT * FROM states AS s \
                WHERE name='{}' ORDER BY s.id".format(argv[4]))
    states = cur.fetchall()

    for state in states:
        if state[1] == argv[4]:
            print(state)

    cur.close()
    conn.close()

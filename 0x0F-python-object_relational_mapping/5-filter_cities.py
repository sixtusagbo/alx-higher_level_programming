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
    cur.execute("SELECT c.id, c.name, s.name\
                FROM cities AS c\
                LEFT JOIN states AS s ON c.state_id = s.id\
                WHERE s.name=%s\
                ORDER BY c.id;", (argv[4], ))
    query_rows = cur.fetchall()

    print(", ".join([row[1] for row in query_rows]))

    cur.close()
    conn.close()

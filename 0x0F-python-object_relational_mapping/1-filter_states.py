#!/usr/bin/python3

"""
A script that lists all states from the database hbtn_0e_0_usa
starting with capital letter N
Username, password and database are given as user args
"""

import sys
import MySQLdb

if __name__ == '__main__':
    db = MySQLdb.connect(user=sys.argv[1],
            passwd=sys.argv[2],
            db=sys.argv[3],
            host='localhost',
            port=3306)

    cur = db.cursor()

    cur.execute("SELECT * FROM states\
            WHERE name LIKE BINARY 'N%' ORDER BY states.id in ACS")

    data = cur.fetchall()

    for row in data:
        print(row)

    cur.close()
    db.close()

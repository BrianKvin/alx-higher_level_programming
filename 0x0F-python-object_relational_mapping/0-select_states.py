#!/usr/bin/python3

"""
This script lists all states from the database 'hbtn_0e_0_usa'
"""
import MySQLdb
import sys

if __name__ == '__main__':
    """
    Access to the database amd get the states
    from the database
    """
    db = MySQLdb.connect(host="localhost",
            port=3306,
            user=sys.argv[1],
            passwd=sys.argv[2],
            db=sys.argv[3])

    cursor = db.cursor()
    cursor.execute("SELECT * FROM states ORDER BY id ASC")
    data = cursor.fetchall()

    for row in data:
        print(row)

    cursor.close()
    db.close()

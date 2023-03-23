#!/usr/bin/python3
"""takes in arguments and displays all values in the states\
    table of hbtn_0e_0_usa where name matches the argument"""

import MySQLdb
import sys

if __name__ == '__main__':
    db = MySQLdb.connect(
                        host='localhost',
                        port=3306,
                        user=sys.argv[1],
                        passwd=sys.argv[2],
                        db=sys.argv[3])

    cur = db.cursor()
    """The query uses the LIKE operator with the BINARY keyword\
to perform a case-sensitive match of the 'name' column\
against the string specified by the 'argv[4]' argument."""
    cur.execute("SELECT * FROM states WHERE NAME like binary '{}'\
            ORDER BY states.id ASC".format(sys.argv[4]))
    rows = cur.fetchall()
    for row in rows:
        print(row)

    cur.close()
    db.close()

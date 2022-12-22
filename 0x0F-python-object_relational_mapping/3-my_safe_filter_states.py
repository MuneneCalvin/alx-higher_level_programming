#!/usr/bin/python3
"""But this time, write one that is safe from MySQL injections"""


import sys
import MySQLdb


if __name__ == '__main__':
    conn = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2],
                           db=sys.argv[3])
    cur = conn.cursor()
    cur.execute("SELECT * FROM `states` ORDER BY id")
    query_rows = cur.fetchall()
    [print(row) for row in query_rows if row[1] == sys.argv[4]]

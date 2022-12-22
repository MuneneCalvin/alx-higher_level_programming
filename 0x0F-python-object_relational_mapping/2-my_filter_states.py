#!/usr/bin/python3
"""Write a script that takes in an argument and displays all
values in the states table of hbtn_0e_0_usa where name matches the argument.
"""

import sys
import MySQLdb


if __name__ == '__main__':
    conn = MySQLdb.connect(user=sys.argv[1],
                           passwd=sys.argv[2], db=sys.argv[3])
    cur = conn.cursor()
    cur.execute("SELECT * FROM `states`\
                 WHERE `name`='{}' ORDER BY `id`".format(sys.argv[4]))
    query_rows = cur.fetchall()
    [print(row) for row in query_rows]

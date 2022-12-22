#!/usr/bin/python3
"""Write a script that takes in the name of a state
as an argument and lists all cities of that state,
using the database hbtn_0e_4_usa
"""


import sys
import MySQLdb


if __name__ == '__main__':
    conn = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2],
                           db=sys.argv[3])
    cur = conn.cursor()
    cur.execute("SELECT * FROM `cities`\
                INNER JOIN `states`\
                ON `states`.`id` = `cities`.`state_id`\
                ORDER BY `cities`.`id`")
    query_rows = cur.fetchall()
    print(", ".join([row[2] for row in query_rows if row[4] == sys.argv[4]]))
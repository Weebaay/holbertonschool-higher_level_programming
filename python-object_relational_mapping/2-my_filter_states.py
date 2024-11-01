#!/usr/bin/python3
"""Module 2-my_filter_states: Filter states by user input"""

import MySQLdb
import sys


db = MySQLdb.connect(
    host="localhost",
    port=3306,
    user=sys.argv[1],
    passwd=sys.argv[2],
    db=sys.argv[3]
)

cursor = db.cursor()

query = "SELECT * FROM states WHERE name = %s ORDER BY id ASC"
cursor.execute(query, (sys.argv[4],))

rows = cursor.fetchall()
for row in rows:
    print(row)

cursor.close()
db.close()

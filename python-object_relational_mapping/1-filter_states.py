#!/usr/bin/python3
"""Modeule 1-filter_states: Define list all states with naming starting with
'N' from database"""


import MySQLdb
import sys

db = MySQLdb.connect(
    host="localhost",
    port=3306,
    user=sys.argv[1],
    passwd=sys.argv[2],
    db="hbtn_0e_0_usa"
)

cursor = db.cursor()

cursor.execute("SELECT * FROM states WHERE name LIKE 'N%' ORDER BY id ASC;")

rows = cursor.fetchall()

for row in rows:
    print(row)

cursor.close()
db.close()

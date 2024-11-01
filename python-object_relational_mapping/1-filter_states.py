#!/usr/bin/python3
"""Module 1-filter_states: Defines a script that lists all states
starting with 'N' from a database in ascending order by id."""

import MySQLdb
import sys


def main():
    """Lists all states from a database starting with 'N'."""
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3]
    )

    cursor = db.cursor()
    cursor.execute(
        "SELECT * FROM states WHERE name LIKE 'N%' ORDER BY id ASC;")
    rows = cursor.fetchall()

    for row in rows:
        print(row)

    cursor.close()
    db.close()


if __name__ == "__main__":
    main()

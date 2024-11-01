#!/usr/bin/python3
"""Module 2-my_filter_states: Lists states with names matching
a user-provided argument from a database, in ascending order by id."""

import MySQLdb
import sys


def main():
    """Lists states with names that match a user-provided argument."""
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3]
    )

    cursor = db.cursor()
    cursor.execute(
        "SELECT * FROM states WHERE name = %s ORDER BY id ASC;", (sys.argv[4],))
    rows = cursor.fetchall()

    for row in rows:
        print(row)

    cursor.close()
    db.close()


if __name__ == "__main__":
    main()

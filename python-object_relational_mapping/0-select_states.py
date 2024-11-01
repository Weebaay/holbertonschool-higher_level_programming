#!/usr/bin/python3
"""Module 0-select_states: Defines a script that lists all states
from a database."""

import MySQLdb
import sys


def main():
    """Connect to the database, fetch all states, and print them."""
    try:
        db = MySQLdb.connect(
            host="localhost",
            port=3306,
            user=sys.argv[1],
            passwd=sys.argv[2],
            db=sys.argv[3]
        )

        cursor = db.cursor()
        cursor.execute("SELECT * FROM states ORDER BY id ASC;")
        rows = cursor.fetchall()
        for row in rows:
            print(row)

        cursor.close()
        db.close()
    except IndexError:
        pass


if __name__ == "__main__":
    main()

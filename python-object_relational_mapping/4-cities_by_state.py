#!/usr/bin/python3
"""Module 4-cities_by_state: Lists all cities from a
database with their states"""

import MySQLdb
import sys


def main():
    """Lists all cities with their associated state from a database."""
    db = MySQLdb.Connect(
        host="localhost",
        port=3306,
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3]
    )

    cursor = db.cursor()

    query = """
        SELECT cities.id, cities.name, states.name
        FROM cities
        JOIN states ON cities.state_id = states.id
        ORDER BY cities.id ASC
    """

    cursor.execute(query)

    rows = cursor.fetchall()
    for row in rows:
        print(row)


if __name__ == "__main__":
    main()

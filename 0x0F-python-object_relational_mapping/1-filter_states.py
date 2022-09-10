#!/usr/bin/python3
"""
Lists all states with a name starting with N (upper N)
"""
import sys
import MySQLdb

host = "localhost"
port = 3306

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("USAGE: ./0-select_states.py user passwd database")
        sys.exit(1)

    user, passwd, db = sys.argv[1], sys.argv[2], sys.argv[3]

    db = MySQLdb.connect(host=host, user=user, passwd=passwd, db=db)
    cur = db.cursor()
    query = """
    SELECT * FROM states
    WHERE name like 'N%'
    ORDER BY id ASC;
    """
    cur.execute(query)
    rows = cur.fetchall()
    for row in rows:
        print(row)

    cur.close()
    db.close()

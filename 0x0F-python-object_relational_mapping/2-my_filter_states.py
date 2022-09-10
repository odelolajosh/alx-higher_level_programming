#!/usr/bin/python3
"""
Lists all states with a name starting with N (upper N)
"""
import sys
import MySQLdb

host = "localhost"
port = 3306

if __name__ == "__main__":
    if len(sys.argv) != 5:
        print("USAGE: ./0-select_states.py user passwd database search_string")
        sys.exit(1)

    user, passwd, db, term = sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4]

    db = MySQLdb.connect(host=host, user=user, passwd=passwd, db=db)
    cur = db.cursor()

    query = """
    SELECT * FROM states
    WHERE CONVERT(`name` USING Latin1)
    COLLATE Latin1_General_CS
    = '{}';
    """.format(term)

    cur.execute(query)
    rows = cur.fetchall()
    for row in rows:
        print(row)

    cur.close()
    db.close()

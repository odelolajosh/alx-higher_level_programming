#!/usr/bin/python3
import sys
import MySQLdb

if len(sys.argv) != 4:
    print("USAGE: ./0-select_states.py user passwd database")
    sys.exit(1)

host = "localhost"
port = 3306
user, passwd, db = sys.argv[1], sys.argv[2], sys.argv[3]

with MySQLdb.connect(host=host, user=user, passwd=passwd, db=db) as db:
    with db.cursor() as cur:
        query = """SELECT * FROM states WHERE name like 'N%' ORDER BY id ASC"""
        cur.execute(query)
        rows = cur.fetchall()
        for row in rows:
            print(row)

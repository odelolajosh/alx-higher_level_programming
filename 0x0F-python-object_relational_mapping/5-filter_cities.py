#!/usr/bin/python3
"""
Lists all cities
"""
import sys
import MySQLdb

host = "localhost"
port = 3306

if __name__ == "__main__":
    if len(sys.argv) != 5:
        print("USAGE: {} user passwd database".format(sys.argv[0]))
        sys.exit(1)

    user, passwd, db, state = sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4]

    db = MySQLdb.connect(host=host, user=user, passwd=passwd, db=db)
    cur = db.cursor()

    query = """
    SELECT `name` FROM `cities`
    WHERE `state_id` = (
        SELECT `id` FROM `states`
        WHERE `name` = %s
    )
    ORDER BY `id` ASC;
    """

    cur.execute(query, (state, ))
    rows = cur.fetchall()
    print(", ".join([row[0] for row in rows]))

    cur.close()
    db.close()

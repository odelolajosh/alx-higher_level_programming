#!/usr/bin/python3
"""
Lists all cities
"""
import sys
import MySQLdb

host = "localhost"
port = 3306

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("USAGE: {} user passwd database".format(sys.argv[0]))
        sys.exit(1)

    user, passwd, db = sys.argv[1], sys.argv[2], sys.argv[3]

    db = MySQLdb.connect(host=host, user=user, passwd=passwd, db=db)
    cur = db.cursor()

    query = """
    SELECT `cities`.`id`, `cities`.`name`, `states`.`name` FROM `cities`
    JOIN `states` ON `states`.`id` = `cities`.`state_id`
    ORDER BY `cities`.`id` ASC;
    """

    cur.execute(query)
    rows = cur.fetchall()
    for row in rows:
        print(row)

    cur.close()
    db.close()

#!/usr/bin/python3
"""
creates the State “California” with the City 'San Francisco'
from the database hbtn_0e_100_usa
"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from relationship_state import Base, State
from relationship_city import City

host = "localhost"

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("USAGE: {} username passwd db".format(sys.argv[0]))
        sys.exit(1)

    user, passwd, db = sys.argv[1], sys.argv[2], sys.argv[3]

    engine = create_engine(
        'mysql+mysqldb://{}:{}@{}/{}'.format(user, passwd, host, db),
        pool_pre_ping=True
    )
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    california_s = State(name="California")
    san_francisco_c = City(name="San Francisco")
    california_s.cities.append(san_francisco_c)

    session.add(california_s)
    session.add(san_francisco_c)
    session.commit()

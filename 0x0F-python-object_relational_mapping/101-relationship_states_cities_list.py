#!/usr/bin/python3
"""
lists all State objects, and corresponding City objects,
contained in the database hbtn_0e_101_usa
"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from relationship_state import State
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

    Session = sessionmaker(bind=engine)
    session = Session()

    states = session.query(State).outerjoin(City).order_by(
        State.id, City.id
        ).all()

    for state in states:
        print("{}: {}".format(state.id, state.name))
        for city in state.cities:
            print("\t{}: {}".format(city.id, city.name))

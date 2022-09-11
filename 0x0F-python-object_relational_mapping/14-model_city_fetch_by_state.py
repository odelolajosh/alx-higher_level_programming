#!/usr/bin/python3
import sys
from model_city import City
from model_state import State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

host = "localhost"

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("USAGE: {} user passwd database".format(sys.argv[0]))
        sys.exit(1)

    user, passwd, db = sys.argv[1], sys.argv[2], sys.argv[3]

    engine = create_engine(
        'mysql+mysqldb://{}:{}@{}/{}'.format(user, passwd, host, db),
        pool_pre_ping=True
    )

    Session = sessionmaker(bind=engine)
    session = Session()

    states_and_cities = session.query(
        State, City
        ).filter(State.id == City.state_id).all()
    for state, city in states_and_cities:
        print("{}: ({}) {}".format(state.name, city.id, city.name))

    session.close()

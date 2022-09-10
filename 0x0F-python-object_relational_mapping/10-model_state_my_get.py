#!/usr/bin/python3
"""
lists all `State` objects that contain the letter a
"""
import sys
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker
from model_state import State

host = "localhost"

if __name__ == "__main__":
    if len(sys.argv) != 5:
        print("USAGE: {} user passwd database".format(sys.argv[0]))
        sys.exit(1)

    user, passwd, db, name = sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4]

    engine = create_engine(
        'mysql+mysqldb://{}:{}@{}/{}'.format(user, passwd, host, db),
        pool_pre_ping=True
    )

    # Create a configured "Session" class
    Session = sessionmaker(bind=engine)

    # Create a session
    session = Session()

    state = session.query(State).filter(State.name == name).first()

    if state:
        print(state.id)
    else:
        print('Not found')

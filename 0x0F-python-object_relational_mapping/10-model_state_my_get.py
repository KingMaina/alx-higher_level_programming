#!/usr/bin/python3

"""Prints the name of a state passed as an argument
Usage:
    ./10-model_state_my_get.py <user> <password> <database_name> <state_name>
"""
import sys
from sqlalchemy import (create_engine)
from sqlalchemy.orm import Session
from model_state import State, Base


if __name__ == "__name__":
    db_uri = 'mysql+mysqldb://{}:{}@localhost/{}'.format(
        sys.argv[1], sys.argv[2], sys.argv[3], pool_pre_ping=True
    )
    engine = create_engine(db_uri)
    Base.metadata.create_all(engine)
    session = Session(engine)
    query = session.query(State).filter(
        State.name.like("%{}%".format(sys.argv[4])))
    state = query.first()
    if state is None:
        print("Not found")
    else:
        print(state.id)
    session.close()
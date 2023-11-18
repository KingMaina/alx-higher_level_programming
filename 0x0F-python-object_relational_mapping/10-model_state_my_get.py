#!/usr/bin/python3

"""Prints the name of a state passed as an argument
Usage:
    ./10-model_state_my_get.py <user> <password> <database_name> <state_name>
"""
from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from model_state import State, Base


if __name__ == "__name__":
    db_uri = 'mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
        argv[1], argv[2], argv[3]
    )
    engine = create_engine(db_uri, pool_pre_ping=True)
    Base.metadata.create_all(engine)
    session = Session(engine)
    query = session.query(State).filter(
        State.name.like("%{}%".format(argv[4]))).first()
    if query is None:
        print("Not found")
    else:
        print(query.id)
    session.close()

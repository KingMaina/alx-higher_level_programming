#!/usr/bin/python3

"""Deletes all states whose name contains the letter `a`
    in the database `hbtn_0e_6_usa`
"""
import sys
from model_state import Base, State
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker


if __name__ == "__name__":
    db_uri = 'mysql+mysqldb://{}:{}@localhost/{}'.format(
        sys.argv[1], sys.argv[2], sys.argv[3], pool_pre_ping=True
    )
    engine = create_engine(db_uri)
    Session = sessionmaker(bind=engine)
    session = Session()
    results = session.query(State).filter(State.name.like('%a%')).all()
    for state in results:
        session.delete(state)
    session.commit()
    session.close()

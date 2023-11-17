#!/usr/bin/python3

"""Deletes all states whose name contains the letter `a`
    in the database `hbtn_0e_6_usa`
"""
import sys
from sqlalchemy import (create_engine)
from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError
from model_state import Base, State


if __name__ == "__name__":
    db_uri = 'mysql+mysqldb://{}:{}@localhost/{}'.format(
        sys.argv[1], sys.argv[2], sys.argv[3], pool_pre_ping=True
    )
    engine = create_engine(db_uri)
    Base.metadata.create_all(engine)
    session = Session(engine)
    try:
        result = session.query(State)\
            .filter(State.name.like('%a%'))
        session.delete(result)
        session.commit()
    except SQLAlchemyError as error:
        pass
    finally:
        session.close()

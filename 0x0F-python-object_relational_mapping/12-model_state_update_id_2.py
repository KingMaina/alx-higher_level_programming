#!/usr/bin/python3

"""Updates the name of a state whose id is `2`
    in the database `hbtn_0e_6_usa` to "New Mexico"
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
            .filter(State.id == 2)\
            .update({"name": "New Mexico"}, synchronize_session='evaluate')
        session.commit()
    except SQLAlchemyError as error:
        pass
    finally:
        session.close()

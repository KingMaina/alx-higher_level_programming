#!/usr/bin/python3

"""Lists all states and their corresponding cities
    from the database `hbtn_0e_101_usa`
"""

from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import Session

Base = declarative_base()


if __name__ == "__main__":
    db_uri = 'mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
        argv[1], argv[2], argv[3])
    engine = create_engine(db_uri, pool_pre_ping=True)
    Base.metadata.create_all(engine)
    session = Session(bind=engine)

    # query = session.query()
    session.close()

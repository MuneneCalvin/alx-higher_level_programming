#!/usr/bin/python3
"""Write a script that prints the State object
with the name passed as argument from the database hbtn_0e_6_usa
"""


import sys
from sqlalchemy import create_engine
from model_state import State, Base
from sqlalchemy.orm import sessionmaker


if __name__ = '__main__':
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(sys.argv[1], sys.argv[2],
                                   sys.argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()
    n = 0
    for ids in session.query(State):
        if ids.name == sys.argv[4]:
            print("{}".format(ids.id))
            n = 1
            break
    if n == 0:
        print('Not found')

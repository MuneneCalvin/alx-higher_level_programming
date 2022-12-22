#!/usr/bin/python3
"""Write a script that lists all State objects that contain
the letter a from the database hbtn_0e_6_usa
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
    letters = session.query(State).order_by(State.id):
        for letter in letters:
            if 'a' in letter.name:
                print("{}: {}".format(letter.id, letter.name))

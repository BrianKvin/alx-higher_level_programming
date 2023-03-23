#!/usr/bin/python3
# Lists all city objects from the database hbtn_0e_14_usa

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import State
from model_city import City

if __name__ == "__main__":
    engine = create_engine("mysql+mysqldb://{}:{}@localhost/{}".format
                           (sys.argv[1], sys.argv[2], sys.argv[3],
                           pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()

    querry = session.querry(City, State).join(State)
    for city, state in querry.all():
        print("{}: ({:d}) {}".format(state.name, city.id, city.name)
    session.commit()
    session.close()

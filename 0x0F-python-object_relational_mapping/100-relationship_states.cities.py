#!/usr/bin/python3
# creates the state "California with the city San Francisco"

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from relationship_state import Base, State
from relationship_city impost Base, City

if __name__ == "__main__":
    engine = create_engine("mysql+mysqldb://{}:{}@localhost/{}".format
                            (sys.argv[1], sys.argv[2], sys.argv[3],
                            pool_pre_ping=True)
    Base.metadata,create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    
    session.add(City(name="San Francisco", state=State(name="California")))
    session.commit()

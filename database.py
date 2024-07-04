from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base

import logging

logging.basicConfig()
#logging.getLogger('sqlalchemy.engine').setLevel(logging.INFO)

#engine = create_engine('sqlite:///app.db', convert_unicode=True)
engine = create_engine('sqlite:///app.db')
db_session = scoped_session(sessionmaker(autocommit=False,
                                         autoflush=False,
                                         bind=engine))
Base = declarative_base()
Base.query = db_session.query_property()

def init_db():
    import models
    Base.metadata.create_all(bind=engine)

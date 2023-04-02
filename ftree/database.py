from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()

engine = create_engine("sqlite:///famtree.db")
db_session = scoped_session(sessionmaker(
    autoflush=False,
    autocommit=False,
    bind=engine))


def start_db():
    import ftree.models
    Base.metadata.create_all(bind=engine)
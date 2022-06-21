from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import Session
engine = create_engine('postgresql+pg8000://postgres:mysecretpassword@db/postgres', echo=True)

Base = declarative_base()

class Author(Base):
    __tablename__ = "author"
    author_id = Column(Integer, primary_key=True)
    first_name = Column(String)
    last_name = Column(String)

author_1 = Author(
    author_id=1,
    first_name="Piotr",
    last_name="Grohs")
author_2 = Author(
    author_id=2,
    first_name="Jan",
    last_name="Kowalski"
)
with Session(engine) as session:
    session.add(author_2)   
    session.commit()
from sqlalchemy import Column, Integer, String, ForeignKey, create_engine
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from db import engine

class Guest(Base):
    __tablename__ = 'guest'
    
    guest_id = Column(String(20), primary_key=True, autoincrement=True)
    guest_email = Column(String(30))

    def __init__(self, guest_id, guest_email):
        self.guest_id = guest_id
        self.guest_email = guest_email
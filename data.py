import os
import datetime
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy import Table, Column, Integer, String, MetaData, DateTime, Boolean
from sqlalchemy import ForeignKey

engine = create_engine('sqlite:///eTicket.sqlite', echo = False)

Base = declarative_base()

Session = sessionmaker()
Session.configure(bind = engine)
session = Session()


class Event(Base):
    __tablename__ = 'events'

    id = Column(Integer, primary_key = True)
    name = Column(String)
    start_date = Column(DateTime, default = datetime.datetime.now)
    end_date = Column(DateTime, default = datetime.datetime.now)
    venue = Column(String)


class Ticket (Base):
    __tablename__ = 'ticket'
    id = Column(Integer, primary_key = True)
    type = Column(String)
    event_name = Column(String, ForeignKey('events.name'))
    is_valid = Column(Boolean, unique = False, default = True)

    # defines relationship between models
    ticket_id = relationship(Event)

    def __init__(self, type = type, event_name = event_name):
        self.type = type
        self.event_name = event_name


Base.metadata.create_all(engine)
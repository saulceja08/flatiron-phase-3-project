from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime

Base = declarative_base() #Notes: declarative_base() is used to define the main class for creating instances (defien a table)

class User(Base):
    __tablename__ = "users"

    member_id = Column(Integer, primary_key=True, unique=True)
    username = Column(String(25), unique=True, nullable=False)
    password = Column(String(30), unique=False, nullable=False)
    last_name = Column(String(25), unique=False, nullable=True)
    birth_date = Column(DateTime())
    email = Column(String(55), unique=True,nullable=False)
    date_created = Column(DateTime(), default=datetime.utcnow)

    member = relationship("WeightTracker", back_populates="user")

class Workout(Base):
    __tablename__ = 'workouts'

    id = Column(Integer, primary_key=True)
    date = Column(DateTime, default=func.now(), nullable=False)
    duration_minutes = Column(Integer, nullable=False)
    user_id = Column(Integer, ForeignKey('users.id'))

    user = relationship('User', back_populates='workouts')

class WeightTracker(Base):
    id = Column(Integer, primary_key=True, unique=True)
    user_id = Column(Integer, ForeignKey('users.member_id'))
    current_weight = (Integer)
    previous_weight = (Integer)

    user = relationship("User", back_populates='member')

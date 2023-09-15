from sqlalchemy import create_engine, Column, Integer, String, DateTime, ForeignKey, func
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime

Base = declarative_base()

class User(Base):
    __tablename__ = "users"

    member_id = Column(Integer, primary_key=True, unique=True)
    username = Column(String(25), unique=True, nullable=False)
    password = Column(String(30), nullable=False)
    last_name = Column(String(25), nullable=True)
    birth_date = Column(DateTime())
    email = Column(String(55), unique=True, nullable=False)
    date_created = Column(DateTime(), default=datetime.utcnow)

    workouts = relationship("Workout", back_populates="user")
    weight_tracker = relationship("WeightTracker", back_populates="user")

class Workout(Base):
    __tablename__ = 'workouts'

    id = Column(Integer, primary_key=True)
    date = Column(DateTime, default=func.now(), nullable=False)
    duration_minutes = Column(Integer, nullable=False)
    user_id = Column(Integer, ForeignKey('users.member_id'))

    user = relationship('User', back_populates='workouts')

class WeightTracker(Base):
    __tablename__ = 'weight_tracker'

    id = Column(Integer, primary_key=True, unique=True)
    user_id = Column(Integer, ForeignKey('users.member_id'))
    current_weight = Column(Integer)
    previous_weight = Column(Integer)

    user = relationship("User", back_populates='weight_tracker')

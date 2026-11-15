from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class Subject(Base):
    __tablename__ = 'subject'

    subject_id = Column(Integer, primary_key=True)
    subject_title = Column(String, nullable=False)

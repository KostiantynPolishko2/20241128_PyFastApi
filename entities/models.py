from sqlalchemy import Column, Integer, String
from context.database import Base

class Program(Base):
    __tablename__ = 'programs'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    description = Column(String)
    hours = Column(Integer)
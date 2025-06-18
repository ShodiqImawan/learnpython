from sqlalchemy import Column, Integer, String
from database import Base

class User(Base):
    __tablename__ = 'user'

    id = Column(Integer, primary_key = True, index = True)
    username = Column(String(255), unique = True, nullable = False)
    password = Column(String(255), nullable = False)


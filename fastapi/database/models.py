from database.database import Base
from sqlalchemy import Column, Float, String, Integer

class Asset(Base):
    __tablename__ = "assets"
    id = Column(Integer, primary_key=True, index=True)
    type = Column(String(30))
    balance = Column(Float)
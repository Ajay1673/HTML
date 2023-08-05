from sqlalchemy.schema import Column
from sqlalchemy.types import String, Integer
from database import Base,db_engine

class Customer(Base):
    __tablename__ = "Customer"
    
    name = Column(String(25))
    phone = Column(String(10),primary_key=True)
    email = Column(String(30))
    password = Column(String(16))
    status = Column(String(10))

class Booking(Base):
    __tablename__ = "Booking"

    id = Column(Integer,primary_key=True,index=True)
    material = Column(String(20))
    mimg = Column(String(30))
    color = Column(String(20))
    size = Column(String(10))
    date = Column(String(10))
Base.metadata.create_all(bind=db_engine)
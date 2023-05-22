
from sqlalchemy  import create_engine, Column, String, Integer, Float
from sqlalchemy.orm import declarative_base, sessionmaker

Base= declarative_base()


class Employee(Base):

    __tablename__ = 'employees'

    id = Column(Integer, primary_key=True)
    first_name = Column(String)
    last_name = Column(String)
    email = Column(String)
    age = Column(Integer)
    gender =Column(String)
    phone_number = Column(Integer)
    salary = Column(Float)
    designation = Column(String)



engine = create_engine('sqlite:///db.db')

Base.metadata.create_all(engine)

Session = sessionmaker(bind = engine)

session = Session()



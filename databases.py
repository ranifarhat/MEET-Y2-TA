from model import Base, User

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine=create_engine('sqlite:///data.db', echo=True, connect_args={"check_same_thread": False})
Base.metadata.create_all(engine)
DBSession = sessionmaker(bind=engine)
session = DBSession()

def add_user(input_email, input_username):
    user_object = User(
        email=input_email,
        username=input_username)
    session.add(user_object)
    session.commit()

def query_all():
  users = session.query(User).all()
  return users

def get_user(username):
    return session.query(User).filter_by(username=username).first()

def print_all():
	print(session.query(User).all())

for prod in query_all():
    print(prod.username, prod.id, prod.email)

def remove_all():
	session.query(User).delete()
	session.commit()

# remove_all()

# for prod in query_all():
#     print(prod.username, prod.id)
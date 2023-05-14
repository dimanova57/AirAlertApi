from database import session, Region

user = session.query(Region).first()


print(user)
from .db import db


# @models
class Test(db.Document):
    name = db.StringField(required=True)

class User(db.Document):
    email=db.EmailField(required=True, unique=True)
    password=db.StringField(required=True)
    def check_password(self, password):
        return password == self.password

class Company(db.Document):
    name=db.StringField(required=True)
    location=db.StringField(required=True)
    industry=db.StringField(required=True)
    user_id=db.ReferenceField(User, required=True)
    website=db.StringField(required=True)
    founded_year=db.StringField(required=True)
    hrName=db.StringField(required=True)
    
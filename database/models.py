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

class Jobs(db.Document):
    company_id=db.ReferenceField(Company, required=True)
    title=db.StringField(required=True)
    description=db.StringField(required=True)
    requirements=db.StringField(required=True)
    salary=db.StringField(required=True)
    jobtype=db.StringField(required=True)
    status=db.StringField(required=True)
    location=db.StringField(required=True)
    postedDate=db.StringField(required=True)

class Application(db.Document):
    job_id=db.ReferenceField(Jobs, required=True)
    applicant_name=db.StringField(required=True)
    applicant_about=db.StringField(required=True)
    applicant_email=db.StringField(required=True)
    status=db.StringField(required=True)
    applicant_portfolio=db.StringField(required=True)
    appliedDate=db.StringField(required=True)
   
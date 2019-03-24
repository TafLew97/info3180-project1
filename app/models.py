#from sqlalchemy import Column, Integer, String
from . import db

class UserProfile(db.Model):
    import datetime
    __tablename__ = 'profiles'
    id            = db.Column(db.Integer, primary_key=True)
    firstname     = db.Column(db.String(80))
    lastname      = db.Column(db.String(80))
    email         = db.Column(db.String(80),unique=True)
    location      = db.Column(db.String(80))
    biography     = db.Column(db.String(255))
    gender        = db.Column(db.String)
    created_on    = db.Column(db.DateTime)
    filename      = db.Column(db.String())

    def __init__(self,firstname,lastname,gender,email,location,biography,filename,created_on):
        self.firstname=firstname
        self.lastname =lastname
        self.gender=gender
        self.email=email
        self.location=location
        self.biography=biography
        self.filename=filename
        self.created_on=created_on
        
    def get_id(self):
        try:
            return unicode(self.id)  # python 2 support
        except NameError:
            return str(self.id)  # python 3 support
            
    def __repr__(self):
        return '<User %r>' % (self.username)
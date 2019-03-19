from sqlalchemy import Column, Integer, String, DateTime
from . import db

class Profile(db.Model):
    __tablename__ = 'profiles'
    id = Column(Integer, primary_key=True)
    firstname = Column(String)
    lastname = Column(String)
    email = Column(String)
    location = Column(String)
    biography = Column(String)
    gender = Column(String)
    created_on = Column(DateTime)
    
    def __repr__(self):
        return '<Profile id={} firstname={} lastname={} email={} location={} gender={}\nbio={}'.format(
            self.id, self.firstname, self.lastname, self.email, self.location, self.gender, self.biography)
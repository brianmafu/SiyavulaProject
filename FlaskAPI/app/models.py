"""SQLAlchemy database models."""
import datetime


from flask_migrate import Migrate
from flask import Flask

from sqlalchemy import Column, Integer, String, DateTime
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql.sqltypes import DateTime

from .database import DATABASE_URL



app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = DATABASE_URL
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
db = SQLAlchemy(app)
migrate = Migrate(app, db)


def dump_datetime(value):
    """Deserialize datetime object into string form for JSON processing."""
    if value is None:
        return None
    return [value.strftime("%Y-%m-%d"), value.strftime("%H:%M:%S")]

class ListItem(db.Model):
    """List Item Model"""
    __tablename__ = "ListItems"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(1000), index=True)
    date_added = Column(DateTime)

    @property
    def serialize(self):
       """Return object data in easily serializable format"""
       return {
           'id' : self.id,
           'name': self.name,
           'date_added': dump_datetime(self.date_added),
       }


db.create_all()

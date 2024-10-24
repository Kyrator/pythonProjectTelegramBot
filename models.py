
from peewee import *

db = SqliteDatabase('my_app.db')

# User >- History -< Hotel -< Photo


class BaseModel(Model):
    class Meta:
        database = db


class Hotel(Model):
    title = TextField()
    link_booking = TextField()
    describe = TextField()
    price = TextField()
    photo = TextField()
    position = TextField()
    counter_view = TextField()


class History(Model):
    date_search = TextField()
    link_booking = TextField()
    describe = TextField()
    price = TextField()
    photo = TextField()
    position = TextField()


class Photo(Model):
    describe = TextField()

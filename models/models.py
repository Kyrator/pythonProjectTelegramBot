
from peewee import *

db = SqliteDatabase('my_app.db')

# History -< Hotel -< Photo


class BaseModel(Model):
    class Meta:
        database = db


class History(Model):
    user_id = TextField()
    date= TextField()
    link_booking = TextField()
    desc = TextField()
    price = TextField()
    position = TextField()


class Photo(Model):
    link = TextField()
    history = ForeignKeyField(History, )


# создание таблиц, если их нет
Photo.create_table()
History.create_table()
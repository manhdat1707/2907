from os import name
import redis
from flask import Flask,jsonify,request,Response
from peewee import *
import json



# connect database
#
db = MySQLDatabase('dbname', user='root', passwd='my-secret-pw',host='127.0.0.1', port=3307)
class User (Model):
    name = TextField()
    age = CharField()
    class Meta:
      database=db
      db_table='user'
    def json(self):
        return {'id': self.id, 'name': self.name,'age': self.age}


    def get_list_user():
        data_select = list(User.select().dicts())
        return data_select
    def update_one_user(id, name, age):
       q = User.update(name=name, age=age).where(User.id == id)
       q.execute() 

  

db.connect()
db.create_tables([User])




r = redis.Redis(host='127.0.0.1', port=6379)
        
app = Flask(__name__)


@app.before_request
def _db_connect():
    db.connect()


@app.teardown_request
def _db_close(exc):
    if not db.is_closed():
        db.close()

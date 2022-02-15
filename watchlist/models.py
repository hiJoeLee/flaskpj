from werkzeug.security import generate_password_hash,check_password_hash
from flask_login import UserMixin
from watchlist import db



class User(db.Model,UserMixin):#创建的表名为user
    id = db.Column(db.Integer,primary_key=True)#整型，主键
    name = db.Column(db.String(20))
    username = db.Column(db.String(20))
    password_hash = db.Column(db.String(128))
    def set_password(self,password):
        self.password_hash =generate_password_hash(password)
    def validate_password(self,password):
        return check_password_hash(self.password_hash,password)

class Movie(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    title = db.Column(db.String(60))
    year = db.Column(db.String(4))

class Books(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    publish = db.Column(db.Boolean) #布尔值
    date = db.Column(db.DateTime) #时间日期
    content = db.Column(db.Text) #长文本
    price = db.Column(db.Float) #浮点数
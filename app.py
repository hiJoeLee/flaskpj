from flask import Flask,render_template
import os,sys,click
from flask_sqlalchemy import SQLAlchemy  # 导入扩展类


# 导入flask类,创建对象app
app = Flask(__name__)

#配置数据库
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(app.root_path, 'data.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  # 关闭对模型修改的监控
# 在扩展类实例化前加载配置
db = SQLAlchemy(app)

class User(db.Model):#创建的表名为user
    id = db.Column(db.Integer,primary_key=True)#整型，主键
    name = db.Column(db.String(20))

class Movie(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    title = db.Column(db.String(60))
    year = db.Column(db.String(4))

class Book(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    publish = db.Column(db.Boolean) #布尔值
    date = db.Column(db.DateTime) #时间日期
    content = db.Column(db.Text) #长文本
    price = db.Column(db.Float) #浮点数

@app.cli.command() # 注册命令
@click.option('--drop', is_flag=True, help='Create after drop.')  # 设置选项
def initdb(drop):
    if drop:
        db.drop_all()
    db.create_all()
    click.echo("Initialized database.")


def forge():
    db.create_all()
    name = 'joe'
    movies =[
        {'title': 'My Neighbor Totoro', 'year': '1988'},
        {'title': 'Dead Poets Society', 'year': '1989'},
        {'title': 'A Perfect World', 'year': '1993'},
        {'title': 'Leon', 'year': '1994'},
        {'title': 'Mahjong', 'year': '1996'},
        {'title': 'Swallowtail Butterfly', 'year': '1996'},
        {'title': 'King of Comedy', 'year': '1999'},
        {'title': 'Devils on the Doorstep', 'year': '1999'},
        {'title': 'WALL-E', 'year': '2008'},
        {'title': 'The Pork of Music', 'year': '2012'},
        {'title':'JOE','year':'1988'},
    ]

    user = User(name=name)
    db.session.add(user)
    for m in movies:
        movie = Movie(title=m['title'],year=m['year'])
        db.session.add(movie)

    db.session.commit()
    click.echo('Done.')

# 程序路由，设置访问地址
@app.route('/')
def index():
    user = User.query.first() #读取第一条用户记录
    movies = Movie.query.all()  #读取所有电影记录
    # 返回值中使用函数渲染页面并传入参数
    return render_template("index.html", user = user ,movies = movies)

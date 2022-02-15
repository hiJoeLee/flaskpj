from flask import Flask
import os,sys
from flask_sqlalchemy import SQLAlchemy  # 导入扩展类
from flask_login import LoginManager

# 导入flask类,创建对象app
app = Flask(__name__)
#配置数据库
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + 'C://Users//joe//PycharmProjects//flaskpj//data.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  # 关闭对模型修改的监控
app.config['SECRET_KEY'] = 'dev'  # 等同于 app.secret_key = 'dev'

# 在扩展类实例化前加载配置
db = SQLAlchemy(app)
login_manager = LoginManager(app)


@login_manager.user_loader
def load_user(user_id):
  from watchlist.models import User
  user=User.query.get(int(user_id))
  return user

login_manager.login_view = 'login'

@app.context_processor #注册一个模板上下午的处理函数
def inject_user():
  from watchlist.models import User
  user = User.query.first()
  return dict(user=user)#返回字典

from watchlist import views,error,commands
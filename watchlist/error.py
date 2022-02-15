from flask import render_template
from  watchlist import app
# from watchlist.models import User

@app.errorhandler(404)#传入错误处理代码
def page_not_found(e):
    # user = User.query.first()
    return render_template('errors/404.html'),404 #返回模板和400状态码
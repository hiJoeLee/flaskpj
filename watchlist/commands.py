import click
from watchlist import app,db
from watchlist.models import User,Movie,Books

@app.cli.command() # 注册命令
@click.option('--drop', is_flag=True, help='Create after drop.')  # 设置选项
def initdb(drop):
    if drop:
        db.drop_all()
    db.create_all()
    click.echo("Initialized database.")


@app.cli.command()
def forge():
    db.create_all()
    name = '富丽楼业主'
    movies =[
        {'title': '粤AX1111', 'title1':'粤BX2222','year': '13822221111'},

    ]
    books =[
        {'publish':True,'date':1988-1-1,'content':'aaa','price':180.5},
        {'publish':True,'date':1987-2-2,'content':'bbb','price':230.8},
    ]
    user = User(name=name)
    db.session.add(user)
    for m in movies:
        movie = Movie(title=m['title'],title1=m['title1'],year=m['year'])
        db.session.add(movie)
    for k in books:
        book = Books(publish = k['publish'],price = k['price'])
        db.session.add(book)
    db.session.commit()
    click.echo('Done.')


@app.cli.command()
@click.option('--username', prompt=True, help='The username used to login.')
@click.option('--password', prompt=True, hide_input=True, confirmation_prompt=True, help='The password used to login.')
def admin(username, password):
    """Create user."""
    db.create_all()
    user = User.query.first()
    if user is not None:
        click.echo('Updating user...')
        user.username = username
        user.set_password(password)  # 设置密码
    else:
        click.echo('Creating user...')
        user = User(username=username, name='Admin')
        user.set_password(password)  # 设置密码
        db.session.add(user)
    db.session.commit()  # 提交数据库会话
    click.echo('Done.')

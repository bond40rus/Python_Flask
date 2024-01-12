from flask import Flask, render_template, request, url_for
from markupsafe import escape
from models import db, User
from forms import RegisterForm, LoginForm
from flask_migrate import Migrate

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'

db.init_app(app)
migrate = Migrate(app, db)


@app.context_processor
def menu_items():
    menu_items = [
        {'name': 'Home', 'url': url_for("index")},
        {'name': 'Task 1', 'url': url_for("base")},
    ]
    return dict(menu_items=menu_items)


@app.route('/')
def index():
    return 'Hi!'


@app.cli.command("init-db")
def init_db():
    # создать все таблицы
    db.create_all()
    # print('OK')


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if request.method == 'POST':  # если нажали на кнопку
        username = request.form.get('username')
        password = request.form.get('password')
        if (username, password) in db():
            return "Вы вошли "
        return f'неправильный {escape(username)} логин или пароль'
    return render_template('login.html')


@app.route('/register/', methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    if request.method == 'POST' and form.validate():
        name = form.name.data
        email = form.email.data
        password = form.password.data

        existing_user = User.query.filter((User.name == name) | (User.email == email)).first()

        if existing_user:
            error_msg = 'Username or email already exists.'
            form.name.errors.append(error_msg)
            return render_template('register.html', form=form)

        user = User(name=name, email=email, password=password)
        user.set_password(password)
        db.session.add(user)
        db.session.commit()
        return 'Registered success!'
    return render_template('register.html', form=form)


if __name__ == '__main__':
    db.create_all()
    app.run(debug=True)

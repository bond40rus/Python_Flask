from flask import Flask, render_template, request, redirect, url_for, make_response

app = Flask(__name__)


@app.context_processor
def menu():
    menu_items = [
        {'name': 'Home', 'url': url_for("index")},
        {'name': 'Home work 2', 'url': url_for("base_hm2")},
    ]
    return dict(menu_items=menu_items)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/base_hm2')
def base_hm2():
    return render_template('base_hm2.html')

@app.route('/home_work_2', methods=['GET', 'POST'])
def home_work_2():
    if request.method == 'POST':

        user_new = request.form.get('user')
        mail_new = request.form.get('mail')
        response = make_response(redirect(url_for('hello', name=user_new)))

        response.set_cookie(mail_new, user_new)
        return response #redirect(url_for('hello', name=mail_new))
    return render_template('home_work_2.html')


@app.route('/hello/<name>')
def hello(name):
    n = request.cookies.get(name) # возвращает None
    return f'Привет, {name}!'


if __name__ == '__main__':
    app.run(debug=True)

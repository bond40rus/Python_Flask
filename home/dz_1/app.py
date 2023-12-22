from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/about/')
def about():
    return render_template('about.html')


@app.route('/contact/')
def contact():
    return render_template('contact.html')


@app.route('/add-nums/<int:num>/<int:num2>')
def add_nums(num, num2):
    return str(num + num2)


@app.route('/str-len/<str_inp>')
def str_len(str_inp):
    return str(len(str_inp))


@app.route('/students/')
def students():
    _students = [
        {
            "name": "John",
            "surname": "Doe",
            "age": 20,
            "average": 85
        },
        {
            "name": "Jane",
            "surname": "Smith",
            "age": 22,
            "average": 92
        },
    ]
    context = {'students': _students}
    return render_template('students.html', **context)


@app.route('/news/')
def news():
    _news = [
        {
            "title": "John1",
            "descr": "Doe",
            "date": 201
        },
        {
            "title": "John2",
            "descr": "Doe",
            "date": 202
        },
        {
            "title": "John3",
            "descr": "Doe",
            "date": 203
        },
    ]
    context = {'news': _news}
    return render_template('news.html', **context)

@app.route('/shop/')
def shop():
    _category = [
        {
            "name": "Одежда",
            "work_name": "clothes"
        },
        {
            "name": "Обувь",
            "work_name": "boots"
        },
    ]
    context = {'shop': _category}
    return render_template('shop.html', **context)

@app.route('/shop/clothes/')
def clothes():
    _clothes = [
        {
            "name": "Куртка-самокрутка",
            "price": "200"
        },
        {
            "name": "Жомпер",
            "price": "150"
        },
    ]
    context = {'clothes': _clothes}
    return render_template('clothes.html', **context)

@app.route('/shop/boots/')
def boots():
    _boots = [
        {
            "name": "Скороходы",
            "price": "80"
        },
        {
            "name": "Лапти",
            "price": "50"
        },
    ]
    context = {'boots': _boots}
    return render_template('boots.html', **context)


if __name__ == '__main__':
    app.run()

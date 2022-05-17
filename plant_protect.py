from flask import Flask, render_template
from sql_query import items

pp = Flask(__name__)


@pp.route('/')
def home():
    return render_template('home.html')


@pp.route('/index')
def index():
    return render_template('plant.html', items=items)


if __name__ == "__main__":
    pp.run(debug=True)

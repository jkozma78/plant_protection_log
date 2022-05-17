from flask import Flask, render_template

pp = Flask(__name__)


@pp.route('/')
def home():
    items = []
    for i in range(1, 111):
        i = str(i)


        an_item = dict(id=i, date="2012-02-24", chemical="here", plant="waiting", area="fólia", comment="")
        items.append(an_item)

    return render_template('plant2.html', items=items)


if __name__ == "__main__":
    pp.run(debug=True)

from flask import Flask, render_template

pp = Flask(__name__)


@pp.route('/')
def home():
    items = []
    for i in range(1, 111):
        i = str(i)

        # dict == {}
        # you just don't have to quote the keys
        an_item = dict(date="2012-02-" + i, id=i, position="here", status="waiting")
        items.append(an_item)

    return render_template('plant2.html', items=items)


if __name__ == "__main__":
    pp.run(debug=True)

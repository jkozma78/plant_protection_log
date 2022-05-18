from flask import Flask, render_template, request
from sql_query import items


pp = Flask(__name__)

new_record = list()


@pp.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        if request.form['submit_btn'] == 'Show records':
            return render_template('plant.html', items=items)
        else:
            _dated = request.form.get("date")
            _chemical = request.form.get("chemical")
            _plant = request.form.get("plant")
            _area = request.form.get("area")
            _comment = request.form.get("comment")
            if _comment == "":
                _comment = "Nincs"
            new_record=[_dated, _chemical, _plant, _area, _comment]
            # db.create_all()
            # new = PlantProtectionLog(dated=_dated, chemical=_chemical, plant=_plant,
            #                          area=_area,
            #                          comment=_comment)
            # print(new.comment)
            #
            # db.session.add(new)
            # db.session.commit()
    return render_template("home.html")


@pp.route('/index')
def index():
    return render_template('plant.html', items=items)


if __name__ == "__main__":
    pp.run(debug=True)

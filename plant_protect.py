from flask import render_template, request
from sql_query import items
from Flask_sql import *


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
                _comment = "-"

            new = PlantProtectionLog(dated=_dated, chemical=_chemical, plant=_plant, area=_area, comment=_comment)

            db.session.add(new)
            db.session.commit()

            ids = (len(items)) + 1
            items.append(
                {"id": ids, "dated": _dated, "chemical": _chemical, "plant": _plant, "area": _area,
                 "comment": _comment})

    return render_template("home.html")


@pp.route('/plant')
def index():
    return render_template('plant.html', items=items)


if __name__ == "__main__":
    pp.run(port=5000, debug=True)
    #pp.run(host='127.0.0.1', port=5001, debug=True)

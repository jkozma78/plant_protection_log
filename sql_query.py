from Flask_sql import *
# from sqlalchemy import exc

db.create_all()


items = []
for i in PlantProtectionLog.query.all():
    an_item = dict(id=i.id, date=i.date, chemical=i.chemical, plant=i.plant, area=i.area, comment=i.comment)
    items.append(an_item)
# try:
#     new = User(vatnumber='12345678-3-92', persons="Békés Csaba", address="Tb.")
#     db.session.add(new)
#     db.session.commit()
# except exc.SQLAlchemyError as e:
#     print(e)

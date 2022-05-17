from Flask_sql import *
# from sqlalchemy import exc

db.create_all()

vat = list()
firm = list()
for i in PlantProtectionLog.query.all():
    vat.append(i.id)
    firm.append(i.date)
# try:
#     new = User(vatnumber='12345678-3-92', persons="Békés Csaba", address="Tb.")
#     db.session.add(new)
#     db.session.commit()
# except exc.SQLAlchemyError as e:
#     print(e)

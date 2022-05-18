from Flask_sql import *


db.create_all()


items = []
for i in PlantProtectionLog.query.all():
    an_item = dict(id=i.id, dated=i.dated, chemical=i.chemical, plant=i.plant, area=i.area, comment=i.comment)
    items.append(an_item)

# new = PlantProtectionLog(dated="2015-05-05", chemical="decis", plant="paprika", area="fólia",
#                                  comment="első")
# db.session.add(new)
# db.session.commit()
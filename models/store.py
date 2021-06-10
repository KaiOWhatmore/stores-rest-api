from db import db

class StoreModel(db.Model):
    __tablename__ = 'stores'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))

    #list of many items
    items = db.relationship('ItemModel', lazy='dynamic') # Tells SQLAlchemy what our relationship model is

    def __init__(self, name):
        self.name = name


    def json(self):
        return {'name': self.name, 'items': [item.json() for item in self.items.all()]}

    @classmethod
    def find_by_name(cls, name):
        #this directly translates to what the SQL code does
        return cls.query.filter_by(name=name).first() # SELECT * FROM items WHERE name=name


    def save_to_db(self):
        db.session.add(self)
        db.session.commit()


    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()

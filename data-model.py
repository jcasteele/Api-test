from datetime import datetime
from config import db, marsh

class User(db.Model):
    __tablename__ = "user"
    user_id = db.Column(db.Integer, primary_key = True, unique = True)
    fname = db.Column(db.String(32))
    lname = db.Column(db.String(32))
    address = db.Column(db.String(64))
    city = db.Column(db.String(32))
    state = db.Column(db.String(2))
    createdon = db.Column(db.DateTime, default = datetime.utcnow, onupdate = datetime.utcnow)

class Item(db.Model):
    __tablename__ = "item"
    item_id = db.Column(db.Integer, primary_key = True, unique = True)
    inventory = db.Column(db.Integer)
    description = db.Column(db.String(256))
    cost = db.Column(db.Float)
    createdon = db.Column(db.DateTime, default = datetime.utcnow, onupdate = datetime.utcnow)

class Order(db.Model):
    __tablename__ = "order"
    order_id = db.Column(db.Integer, primary_key = True, unique = True)
    user_id = db.Column(db.Integer)
    item_id = db.Column(db.Integer)
    orderdate = db.Column(db.DateTime, default = datetime.utcnow, onupdate = datetime.utcnow)

class UserSchema(marsh.SQLAlchemyAutoSchema):
    class Meta:
        model = User
        load_instance = True
        sqla_session = db.session

class ItemSchema(marsh.SQLAlchemyAutoSchema):
    class Meta:
        model = Item
        load_instance = True
        sqla_session = db.session

class OrderSchema(marsh.SQLAlchemyAutoSchema):
    class Meta:
        model = Order
        load_instance = True
        sqla_session = db.session

user_schema = UserSchema()
users_schema = UserSchema(many = True)
item_schema = ItemSchema()
items_schema = ItemSchema(many = True)
order_schema = OrderSchema()
orders_schema = OrderSchema(many = True)
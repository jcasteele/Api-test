import sqlite3

connect = sqlite3.connect("test.db")

user_columns = [
    "user_id INTEGER PRIMARY KEY UNIQUE",
    "fname VARCHAR",
    "lname VARCHAR",
    "address VARCHAR",
    "city VARCHAR",
    "state VARCHAR",
    "createdon DATETIME",
]

item_columns = [
    "item_id INTEGER PRIMARY KEY UNIQUE",
    "inventory INTEGER",
    "description VARCHAR",
    "cost FLOAT",
    "createdon DATETIME",
]

order_columns = [
    "order_id INTEGER PRIMARY KEY UNIQUE",
    "user_id INTEGER",
    "item_id INTEGER",
    "orderdate DATETIME",
]

create_user = f"CREATE TABLE user ( {','.join(user_columns)})"
create_item = f"CREATE TABLE item ( {','.join(item_columns)})"
create_order = f"CREATE TABLE order ( {','.join(order_columns)})"

connect.execute(create_user)
connect.execute(create_item)
connect.execute(create_order)
import pathlib
import connexion
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

basedir = pathlib.Path(__file__).parent.resolve()
connex = connexion.App(__name__, specification_dir = basedir)

app = connex.app
app.config["SQLALCHEMY_DATABASE_URI"] = f"sqlite:///{basedir / 'test.db'}"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)
marsh = Marshmallow(app)
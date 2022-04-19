from app import app
from db.db import db


with app.app_context():
    db.create_all()

if "__main__" == __name__:
    app.run(debug=True)

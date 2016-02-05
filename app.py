from flask import Flask, request
from database import db
import user

app = Flask(__name__)

app.config.from_object('config.Config')
db.init_app(app)

@app.route("/")
def hello():
    return "Hello World!"

@app.route("/users", methods=["POST"])
def create_user():
    email = request.form["email"]

    # work with sess
    new_user = user.User(email)
    db.session.add(new_user)
    db.session.commit()

    return "Created User! %s " % email


if __name__ == "__main__":
    app.run(debug=True)

from database import db
from flask import Flask, request
from models import User, Business, Point

app = Flask(__name__)

app.config.from_object('config.Config')
db.init_app(app)


@app.route("/")
def hello():
    return "Hello Fidelity!"


@app.route("/users", methods=["POST"])
def create_user():
    email = request.form["email"]

    new_user = User(email)
    db.session.add(new_user)
    db.session.commit()

    return "Created User! %s " % email


@app.route("/users/<int:id>", methods=["GET"])
def get_user(id):
    user = User.query.get(id)

    return "user: %s" % user.email


@app.route("/business", methods=["POST"])
def create_business():
    name = request.form["name"]
    points = request.form["points"]

    new_business = Business(name, points)
    db.session.add(new_business)
    db.session.commit()

    return "Created Business! %s " % name


@app.route("/business/<int:id>", methods=["GET"])
def get_business(id):
    business = Business.query.get(id)

    return "business: %s" % business.email


@app.route("/user/<int:user_id>/business/<int:business_id>", methods=["POST"])
def add_point(user_id, business_id):
    new_point = Point(user_id, business_id)
    db.session.add(new_point)
    db.session.commit()

    return "Point added!"


if __name__ == "__main__":
    app.run(debug=True)

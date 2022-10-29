from flask import Flask, redirect, url_for, render_template, request,jsonify





app = Flask(__name__)
app.config['JSON_SORT_KEYS'] = False
"""
#database connection
SQLALCHEMY_DATABASE_URI = "mysql+mysqlconnector://{username}:{password}@{hostname}/{databasename}".format(
    username="Sebas",
    password="FypDatabase",
    hostname="Sebas.mysql.pythonanywhere-services.com",
    databasename="Sebas$FYP",
)
app.config["SQLALCHEMY_DATABASE_URI"] = SQLALCHEMY_DATABASE_URI
app.config["SQLALCHEMY_POOL_RECYCLE"] = 299
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False


engine = db.create_engine(SQLALCHEMY_DATABASE_URI, {})


db.init_app(app)
with app.app_context():
    db.create_all()
"""

"""
build login page then use this function
@app.route('/')
def login_page():
    return render_template("login_page.html")
"""""
@app.route("/", methods = ['POST', 'GET'])
def main():
    return render_template("employee_side/instructions_page.html")
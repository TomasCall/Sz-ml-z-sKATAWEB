import MySQLdb
from flask import Flask, render_template, request, redirect,session
from flask.helpers import url_for
from flask_mysqldb import MySQL


app = Flask(__name__)

app.secret_key = 'your secret key'

app.config['MYSQL_HOST'] = "localhost"
app.config['MYSQL_USER'] = "root"
app.config['MYSQL_PASSWORD'] = ""
app.config['MYSQL_DB'] = "webszamla"

mysql = MySQL(app)


@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template("home.html")



@app.route("/user")
def users():
    if "loggedin" in session:
        return render_template('user.html')
    return redirect(url_for("index"))

@app.route("/bills")
def bills():
    return render_template('bills.html')


@app.route("/login", methods=["GET", "POST"])
def login():
    msg = ''
    if request.method == "POST" and "username" in request.form and "password" in request.form:
        username = request.form["username"]
        password = request.form["password"]
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute("SELECT * FROM user WHERE felhasznalonev = %s AND jelszo = %s", (username, password,))
        account = cursor.fetchone()
        cursor.close()
        if account:
            session["loggedin"] = True
            session["username"] = account["felhasznalonev"]
            return redirect("/user")
        else:
            msg = "Incorrect username/password!"
    return render_template('login.html', msg=msg)



@app.route("/registration", methods=["GET", "POST"])
def registration():
    if request.method == "POST" and request.form["username"] != "" and request.form["email"] is not "" and request.form["password"] is not "":
        userDetails = request.form
        name = userDetails["username"]
        email = userDetails["email"]
        password = userDetails["password"]
        cur = mysql.connection.cursor()
        cur.execute(f"INSERT INTO user(felhasznalonev, email, jelszo) VALUES(\"{name}\",\"{email}\",\"{password}\")")
        mysql.connection.commit()
        cur.close()
        session["loggedin"] = True
        session["username"] = userDetails["username"]
        return redirect("/user")
    return render_template("registration.html")


@app.route("/logout")
def logout():
   session.pop("loggedin", None)
   session.pop("username", None)
   return redirect(url_for("login"))


@app.route("/bills_insert")
def bills_insert():
    return render_template("bills_insert.html")


if __name__ == '__main__':
    app.run(debug=True)
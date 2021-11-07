from datetime import date
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
    if "loggedin" in session:
        cur = mysql.connection.cursor()
        resultValue = cur.execute(f"SELECT szamlaszam,megrendeloneve,osszeg,megrendeles_datuma,hatarido,teljesitve FROM datas where felhasznalonev='{session['username']}'")
        if resultValue>0:
            userDetails = cur.fetchall()
            line_number = range(len(userDetails)+1)[-1]
            cur.close()
            print(len(userDetails[0][4]))
            print(userDetails[0][4])
            print(str(date.today().strftime("Y-M-D")))
            return render_template('bills.html',userDetails=userDetails,line=line_number,today=date.today().strftime('%Y-%m-%d'))
        else:
            return render_template("bills_insert.html")
    else:
        return render_template("home.html")


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


@app.route("/bills_insert",methods=["GET","POST"])
def bills_insert():
    if request.method == "POST" and "loggedin" in session and request.form["Szamlaszam"] != "" and  request.form["Megrendeloneve"] != "" and request.form["Osszeg"] != None and request.form["begining"] != "" and  request.form["Hatarido"] != "":
        bill_details = request.form
        bills_id = bill_details["Szamlaszam"]
        costumer_name = bill_details["Megrendeloneve"]
        amount = bill_details["Osszeg"]
        begining = bill_details["begining"]
        deadline = bill_details["Hatarido"]
        cur = mysql.connection.cursor()
        cur.execute(f"INSERT INTO datas(szamlaszam, osszeg, megrendeloneve, megrendeles_datuma, hatarido,felhasznalonev) VALUES(\"{bills_id}\",{amount},\"{costumer_name}\",\"{begining}\",\"{deadline}\",\"{session['username']}\")")
        mysql.connection.commit()
        cur.close()
        return render_template("bills_insert.html")
    if "loggedin" in session:
        return render_template("bills_insert.html")
    return render_template("home.html")


if __name__ == '__main__':
    app.run(debug=True)
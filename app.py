from flask import Flask, render_template, request, redirect
from flask_mysqldb import MySQL


app = Flask(__name__)

# Configure db
#db = yaml.load(open('db.yaml'))
app.config['MYSQL_HOST'] = "localhost"
app.config['MYSQL_USER'] = "root"
app.config['MYSQL_PASSWORD'] = ""
app.config['MYSQL_DB'] = "webszamla"

mysql = MySQL(app)

@app.route('/', methods=['GET', 'POST'])
def index():
    return "<h1>Main Page</h1>"

@app.route("/users")
def users():
    cur = mysql.connection.cursor()
    resultValue = cur.execute("SELECT * FROM adatok")
    if resultValue > 0:
        userDetails = cur.fetchall()
        return render_template('user.html',userDetails=userDetails)


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        return "Hello World"
    return render_template("login.html")


@app.route("/registration", methods=["GET", "POST"])
def registration():
    if request.method == 'POST':
        # Fetch form data
        userDetails = request.form
        name = userDetails["usr"]
        email = userDetails["mail"]
        password = userDetails["pswd"]
        cur = mysql.connection.cursor()
        cur.execute(f"INSERT INTO user(felhasznalonev, email, jelszo) VALUES(\"{name}\",\"{email}\",\"{password}\")")
        mysql.connection.commit()
        cur.close()
        return "<h1>asd</h1>"
    return render_template("registration.html")


if __name__ == '__main__':
    app.run(debug=True)
from flask import Flask, render_template, request, redirect
from flask_mysqldb import MySQL


app = Flask(__name__)

# Configure db
#db = yaml.load(open('db.yaml'))
app.config['MYSQL_HOST'] = "localhost"
app.config['MYSQL_USER'] = "root"
app.config['MYSQL_PASSWORD'] = ""
app.config['MYSQL_DB'] = "szamla"

mysql = MySQL(app)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Fetch form data
        userDetails = request.form
        name = userDetails['usrn']
        email = userDetails['pswd']
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO asd(a, b) VALUES(%s, %s)",(name, email))
        mysql.connection.commit()
        cur.close()
        return redirect('/users')
    return render_template('login.html')

@app.route('/users')
def users():
    cur = mysql.connection.cursor()
    resultValue = cur.execute("SELECT * FROM adatok")
    if resultValue > 0:
        userDetails = cur.fetchall()
        return render_template('user.html',userDetails=userDetails)

if __name__ == '__main__':
    app.run(debug=True)
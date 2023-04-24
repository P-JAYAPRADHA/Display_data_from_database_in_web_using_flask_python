from flask import Flask, render_template
from flask_mysqldb import MySQL

app=Flask(__name__)

app.config["MYSQL_HOST"] = "localhost"
app.config["MYSQL_USER"] = "root"
app.config["MYSQL_PASSWORD"] = "<your password>"
app.config["MYSQL_DB"] = "information"
app.config["MYSQL_CURSORCLASS"] = "DictCursor"
mysql = MySQL(app)

@app.route("/")
def home():
	return render_template("showusers.html")

@app.route("/showdatas")
def showdatas():
	con = mysql.connection.cursor()
	sql = "SELECT * FROM users"
	con.execute(sql)
	res = con.fetchall()
	return render_template("home.html", datas = res)

if(__name__ == '__main__'):
	app.run(debug = True)

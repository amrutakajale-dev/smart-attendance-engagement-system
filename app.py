import mysql.connector
from flask import Flask, render_template

app = Flask(__name__)

#Database connection
db=mysql.connector.connect(
    host="localhost",
    user="root",
   password="Kajale@2211",
   database="smart_attendance" 
)
cursor=db.cursor()

@app.route("/")
def home():
    return render_template("index.html")

#login page route
@app.route("/login")
def login():
    return render_template("login.html")

if __name__ == "__main__":
    app.run(debug=True)


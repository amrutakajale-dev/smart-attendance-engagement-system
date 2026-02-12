import mysql.connector
from flask import Flask, render_template, request

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
@app.route("/login", methods=["GET","POST"])
def login():
    if request.method == "POST":
        email=request.form["email"]
        password=request.form["password"]

        query = "SELECT * FROM users WHERE email=%s AND password=%s"
        cursor.execute(query, (email,password))
        user = cursor.fetchone()

        if user:
            return "Login Successful !"
        else:
            return "Invalid email or password"
        
    return render_template("login.html")

if __name__ == "__main__":
    app.run(debug=True)


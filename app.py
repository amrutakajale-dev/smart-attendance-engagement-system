import mysql.connector

from flask import Flask, render_template, request,redirect,url_for, session

app = Flask(__name__)

app.secret_key = "secret123"


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

        cursor.execute(
         "SELECT * FROM users WHERE email=%s AND password=%s",
     (email,password)
        )
        user = cursor.fetchone()

        if user:
            session["user"]=user[1]
            return redirect(url_for("dashboard"))
        else:
            return "Invalid email or password"
        
    return render_template("login.html")

#Dashboard route add
@app.route("/dashboard")
def dashboard():
    if "user" in session:
        return f"Welcome {session['user']} to dashboard"
    else:
        return redirect(url_for("login"))
    

#Logout route add
@app.route("/logout")
def logout():
    session.pop("user", None)
    return redirect(url_for("login"))


if __name__ == "__main__":
    app.run(debug=True)


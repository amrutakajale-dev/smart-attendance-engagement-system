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
    message = request.args.get("msg")

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
        
    return render_template("login.html",message=message)

#Add register route
@app.route("/register", methods=["GET","POST"])
def register():
    if request.method == "POST":
        name = request.form["name"]
        email = request.form["email"]
        password = request.form["password"]

        cursor.execute(
            "INSERT INTO users (name, email, password) VALUES (%s,%s,%s)",
            (name, email, password)
        )
        db.commit()

        return redirect(url_for("login", msg="Registerd!"))

    return render_template("register.html")


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


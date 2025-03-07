from flask import Flask , redirect, url_for, render_template ,request ,session, flash
from datetime import timedelta

app = Flask(__name__)
app.secret_key = "hello"
app.permanent_session_lifetime = timedelta(minutes=5)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/login", methods=["POST","GET"])
def login():
    if request.method == "POST":
        session.permanent = True
        user = request.form["nm"]
        session["user"] = user
        flash("Login Succesful!")
        return redirect(url_for("user"))
    else:
        if "user" in session:
            flash("Already Logged In!")
            return redirect(url_for("user"))

        return render_template("login.html")

@app.route("/usr")
def user():
    if "user" in session:
        user = session["user"]
        return render_template("user.html", user=user)
    else:
        flash("Yuo are not logged in!")
        return redirect(url_for("login"))

@app.route("/logout")
def logout():
    if "user" in session:
        user = session["user"]
        flash(f"You have been logged out, {user}", "info")
    session.pop("user", None)
    return redirect(url_for("login"))

if __name__== "__main__":
    app.run(debug=True)

# redirect = เป็นการเปลียนทิศทาง
# url_for = ใส่ url
# render_template = เชื่มกับไฟล์ templates HTML
# request ไว้ดึงข้อมูลจากไฟล์ HTML บน method
# session ไว้เก็บข้อมูล user ชั่วคราว
# flash ข้อความแจ้งเตือน
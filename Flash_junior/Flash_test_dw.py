from flask import Flask , redirect, url_for
# redirect = เป็นการเปลียนทิศทาง
# url_for = ใส่ url

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello this is test web <h1>Hello<h1>"

@app.route("/<name>") # <name> เมื่อใส่อะไรก็ตาม จะขึ้น ตามชื่อที่เขียน
def user(name):
    return f"Hello {name}!"

@app.route("/admin/")
def admin():
    return redirect(url_for("user", name="Admin!"))

if __name__== "__main__":
    app.run()
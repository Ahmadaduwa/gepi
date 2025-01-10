from flask import Flask , redirect, url_for, render_template
# redirect = เป็นการเปลียนทิศทาง
# url_for = ใส่ url
# render_template = เชื่มกับไฟล์ templates HTML

app = Flask(__name__)

@app.route("/<name>")
def home(name):
    return render_template("index.html",content=["tim", "joe", "bill"])

if __name__== "__main__":
    app.run()
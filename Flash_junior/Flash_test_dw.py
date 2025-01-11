from flask import Flask , redirect, url_for, render_template
# redirect = เป็นการเปลียนทิศทาง
# url_for = ใส่ url
# render_template = เชื่มกับไฟล์ templates HTML

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/test")
def test():
    return render_template("new.html", content="Testing")   

if __name__== "__main__":
    app.run(debug=True)
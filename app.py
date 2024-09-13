from flask import Flask, render_template, request 
import sqlite3
con = sqlite3.connect('database.db')
cur = con.cursor()
cur.execute('SELECT * FROM brands')
data = cur.fetchall()
app = Flask(__name__) 
@app.route("/", methods=["GET", "POST"]) 

def index(): 
    if request.method == "POST":
        name = request.form.get("name")
        return render_template("greet.html", name=name)
    return render_template("index.html")

@app.route("/brands", methods=["POST"])
def brands():
    brand = request.form.get("brand")
    if not brand:
         return render_template("error.html", message="you must select a brand")
    else:
        return render_template(brand + ".html", message=brand, data=data)

@app.route("/price", methods=["POST","GET"])
def price():
    return render_template("price.html")


if __name__ == "__main__":
    app.run(debug=True)
from shop import app
from flask import render_template

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/shop")
def shop():
    return render_template('shop.html')

@app.route("/blog")
def blog():
    return render_template('blog.html')


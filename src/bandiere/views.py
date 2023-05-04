from bandiere import app
from bandiere.gestione_bandiere import carica_dizio, akinator

from flask import render_template, request

bandiere = carica_dizio()

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/', methods=['POST'])
def index_post():
    p = request.form['prompt']
    return render_template("index.html", data=akinator(p, bandiere))
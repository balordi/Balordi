from bandiere import app
from bandiere.gestione_bandiere import carica_dizio, akinator

from flask import render_template, request

bandiere = carica_dizio()

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/', methods=['POST'])
def index_post():
    colori = request.form['prompt']
    simbolo = False
    orientamento = request.form['orientamento']

    if request.form.get('simbolo'):
        simbolo = True

    c = [colori, simbolo, orientamento]
    print(str(c))

    return render_template("res.html", data=akinator(c, bandiere))

@app.route('/autori')
def autori():
    return render_template("autori.html")

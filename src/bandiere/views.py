from bandiere import app

from flask import render_template

# bandiere.py
import csv
import pkg_resources

def carica_dizio():
    bandiere = {}
    
    csv_file = pkg_resources.resource_filename('bandiere', 'data/Bandierette.csv')
    
    with open('Bandierette.csv', 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            paese = row[0]
            caratteristiche = row[1:]
            bandiere[paese] = caratteristiche
    return bandiere

def akinator(caratteristiche_input, bandiere):
    for paese, colori_bandiera in bandiere.items():
        if set(caratteristiche_input) == set(colori_bandiera):
            return paese
    return 'Paese non trovato'

bandiere = carica_dizio()

caratteristiche_input = input('Inserisci le caratteristiche della bandiera separati da uno spazio: ').split()

paese_indovinata = akinator(caratteristiche_input, bandiere)
print('La bandiera appartiene a:', paese_indovinata)
# /bandiere.py

@app.route('/')
def index():
    return render_template("index.html")
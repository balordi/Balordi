import csv

def carica_dizio():
    bandiere = {}
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

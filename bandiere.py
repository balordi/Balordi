import csv

def carica_dizio(file_path):
    bandiere = {}
    with open(file_path, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            paese = row[0]
            colori = row[1:]
            bandiere[paese] = colori
    return bandiere

def akinator(colori, bandiere):
    for paese, colori_bandiera in bandiere.items():
        if set(colori) == set(colori_bandiera):
            return paese
    return 'Paese non trovato'

file_path = 'bandierette.csv'
bandiere = carica_dizio(file_path)

colori_input = input('Inserisci i colori della bandiera separati da uno spazio: ').split()
paese_indovinata = akinator(colori_input, bandiere)

print('La bandiera appartiene a:', paese_indovinata)

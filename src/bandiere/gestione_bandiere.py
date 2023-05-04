import csv
import pkg_resources

# Carica il dizionario delle bandiere
def carica_dizio():
    bandiere = {}
    
    csv_file = pkg_resources.resource_filename('bandiere', 'data/Bandierette.csv')
    
    with open(csv_file, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            paese = row[0]
            caratteristiche = row[1:]
            bandiere[paese] = caratteristiche
            print(row)
    return bandiere

# Domanda
def akinator(caratteristiche_input, bandiere):
    caratteristiche_input = str(caratteristiche_input).split()
    for paese, colori_bandiera in bandiere.items():
        if set(caratteristiche_input) == set(colori_bandiera[:-2]):
            return paese
    return 'Paese non trovato'
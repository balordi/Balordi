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
    #caratteristiche_input = str(caratteristiche_input).split()

    for paese, colori_bandiera in bandiere.items():
        caratteristiche_input[1] = str(caratteristiche_input[1])
        print('ce: ' + str(caratteristiche_input))
        print('controllato: ' + str(colori_bandiera))
        if set(caratteristiche_input) == set(colori_bandiera):
            return paese
    return 'Paese non trovato'

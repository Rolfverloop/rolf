import csv

bestand= 'artikelen.csv'

try:
    with open(bestand) as productFile:
        reader=csv.reader(productFile, delimiter=';')

        totaal=0
        artikelnummer=''
        kleinstevoorraad=0
        naam=''
        hoogsteprijs=0
        for row in reader:
            totaal+=int(row[3])
            voorraad=int(row[3])
            if kleinstevoorraad==-1 or voorraad<kleinstevoorraad
                kleinstevoorraad=voorraad
            else:
                if voorraad<kleinstevoorraad:
                    kleinstevoorraad=voorraad
                    artikelnummer=row[0]
            prijs=float(row[4])
            if prijs>hoogsteprijs:
                hoogsteprijs=prijs
                naam=row[2]
        print('Het duurste artikel is Monitorstandaard en die kost {} Euro Er zijn slechts {} exemplaren in voorraad van het product met nummer {} In totaal hebben wij {} producten in ons magazijn liggen').format(naam, str(prijs),str(kleinstevoorraad),artikelnummer, str(totaal))

except IOError:
    print('kan bestand niet lezen')
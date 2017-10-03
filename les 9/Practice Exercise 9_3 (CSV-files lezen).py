import csv

bestand='behaaldescore.csv'

try:
    with open(bestand) as gamersFile:
        reader= csv.reader(gamersFile, delimiter=';')

        hoogstescore=-1
        naam=''
        datum=''
        for row in reader:
            score=int(row[2])
            if score>hoogstescore:
                naam= row[0]
                datum=row[1]
                hoogstescore=score
        print('De hoogste score is {} op datum {} gehaald door {}'.format(str(hoogstescore), datum, naam))

except IOError:
    print('kan bestand niet openen ')
except NameError:
    print('score is onjuist')

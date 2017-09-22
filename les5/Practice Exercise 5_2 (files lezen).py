file=open('/Users/rolfverloop/PycharmProjects/rolf/kaartnummers/klanten', 'r')
lines=file.readlines()
file.close()

for line in lines:
    nummer_naam=line.split(',')
    naam=nummer_naam[1].strip()
    nummer= nummer_naam[0].strip()
    text='{} heeft kaartnummer:{}'.format(naam, nummer)
    print(text)
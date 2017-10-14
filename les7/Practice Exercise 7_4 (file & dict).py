def ticker(bestand):
    bestand=open('market afkortingen','r')
    bestand.read()
    for afkortingen in bestand:
        split=bestand.split(':')
        afkortingenDict={{''}:{}}.format(bestand[0], bestand[1])
    return bestand
    print(afkortingenDict)
    bestand.close()

print(ticker('bestand'))
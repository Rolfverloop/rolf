file=open('/Users/rolfverloop/PycharmProjects/rolf/kaartnummers/klanten', 'r')
lines=file.readlines()
file.close()

regels=0
regelnummer= 0
hoogste=0
for line in lines:
    regels= regels+1
    lijst= line.split(',')
    nummer= int(lijst[0])
    if nummer>hoogste:
        hoogste=nummer
        regelnummer= regels
text='aantal regels is{}, en hoogste isb{}'.format(str(regels), str(hoogste), str(regelnummer))
print(text)
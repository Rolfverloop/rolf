personen= eval(input('met hoeveel personen gaat u reizen?'))
try:
    bedrag= 4356
    antwoord= (bedrag/ personen)
    print('het bedrag per persoon is: {}'.format(antwoord))
except ZeroDivisionError:
        print('U kunt niet delen door nul')
except NameError:
        print('Gebruik cijfers voor het invoeren van het aantal!')


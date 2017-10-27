import random

def monopolyworp():
    while True:
        getal1 =random.randrange(1, 7)
        getal2= random.randrange(1, 7)
        text=''
        if getal1== getal2:
            text= '(gooi nog een keer)'
        print ('{} + {} = {} {}'.format(str(getal1), str(getal2), str(getal1+getal2), text))

monopolyworp()

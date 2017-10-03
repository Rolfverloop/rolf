def code(invoerstring):
    waarde=''
    for c in invoerstring:
        o = ord(c)
        o+=3
        nieuwe_char=chr(o)
        waarde+=waarde+nieuwe_char
    return waarde


text=input('geef naam beginstation eindstation')
antwoord= code(text)
print('code is {}'.format(antwoord))
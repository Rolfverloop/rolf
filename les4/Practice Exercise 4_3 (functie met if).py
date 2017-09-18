lengte=input('Hoe lang ben je:')

def lang_genoeg(lengte):
    if int(lengte)>=120:
        antwoord=('je bent lang genoeg je mag naar binnen')
    if int(lengte)<=120:
        antwoord=('je bent niet lang genoeg, je mag niet naar binnen')
    return antwoord

a=lang_genoeg(lengte)
print(a)

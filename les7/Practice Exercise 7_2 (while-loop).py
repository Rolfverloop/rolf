while True:
    woord=input('geef een woord van vier letters:')
    lengte=len(woord)
    if len(woord)==4:
        print('{} heeft de goede lengte namelijk {}'.format(woord)), str(lengte)
        break
    else:
        print('woord {} heeft niet de goede lengte'.format(woord))
        continue

#er gaat iets fout in de .format str(lengte) maar ik weet niet wat, als het goed is zou het gewoon moeten werken.....
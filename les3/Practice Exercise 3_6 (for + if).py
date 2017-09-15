s ="Guido van Rossum heeft programmeertaal Python bedacht."
for i in s:
    if i.lower() in 'aeiouy':
        print(i)
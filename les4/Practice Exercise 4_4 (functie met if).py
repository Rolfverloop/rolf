oudwachtwoord=input('Wat is je oude wachtwoord:')
nieuwwachtwoord=input('Welk wachtwoord wil je nu:')

def new_pasword(oudwachtwoord, nieuwwachtwoord):
    if oudwachtwoord != nieuwwachtwoord and len(nieuwwachtwoord)>=6:
        antwoord=(True )
    else:
        print(False)
    return antwoord


a=new_pasword(oudwachtwoord, nieuwwachtwoord)
print(a)
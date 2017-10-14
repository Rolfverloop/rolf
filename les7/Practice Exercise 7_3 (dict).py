cijfersDict={'piet':7, 'hans':9, 'rolf':10, 'jan':6 }

def sleutels():
    sleutel=input('geef een geldige code:')
    if sleutel in cijfersDict:
        print(cijfersDict)
    elif TypeError:
        print('dit is geen geldige code')
print(sleutels())


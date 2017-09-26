def seizoen(maand):
    seizoen=''
    if maand>=3 and maand<=5:
        seizoen='lente'
    elif maand >5 and maand <=7:
        seizoen='zomer'
    elif maand>7 and maand<=9:
        seizoen='herfst'
    else:
        seizoen='winter'
    return seizoen

for maand in range(1, 13):
    text='voor maand {} in het seizoen {}'.format(str(maand), seizoen(maand))
    print(text)


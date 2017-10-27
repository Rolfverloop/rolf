grondgetallen=(5, 6, 8, -7, -4,)
def kwadraten_som(grondgetallen):
    totaal=0
    for i in grondgetallen:
      if i >=0:
          totaal+=grondgetallen**2

    return totaal


BLANC = "⬜"
NEGRE = "⬛"
i=0
for x in range(8):
    linia=""
    for y in range(8):
        if i==1:
            linia = linia + BLANC
        else:
            linia = linia + NEGRE
        i=i*-1
    i=i*-1
    print(linia)

ceros=0
positivo=0
negativo=0
for i in range(10):
    num=int(input())
    if num >0:
        positivo=positivo+1
    elif num ==0:
        ceros=ceros+1
    else:
        negativo=negativo+1
print("tienes",positivo,"positivos","tienes",negativo,"negativos","tienes",ceros,"ceros")
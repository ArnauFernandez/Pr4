par=0
impar=0
for i in range(31):
    if i %2==0:
       par=par+i
    else:
        impar=impar+i
print("la suma total de pares es: ",par,"la suma total de impares es: ",impar)

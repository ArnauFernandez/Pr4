"""
Arnau Fernández Pinar
Matteo Vilchez
e2. Programa que mostra un triangle amb nombres a les cantonades.
Cal demanar quina alçada ha de tenir el triangle.
Els valors permesos per a l'alçada son entre 2 i 9.
(ambdós inclosos)
28/11/2023
"""
altura=int(input())
if altura >=2 and altura <=9:
    for i in range(1,altura):
        for j in range(1,altura+1):
            print(j*altura)
else:
    print("error")
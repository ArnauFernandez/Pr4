"""
Arnau Fernández Pinar
Matteo Vilchez
e2. Programa que mostra un triangle amb nombres a les cantonades.
Cal demanar quina alçada ha de tenir el triangle.
Els valors permesos per a l'alçada son entre 2 i 9.
(ambdós inclosos)
28/11/2023
"""
num = int(input("Ingrese un número entre 2 y 9: "))
if num >= 2 and num <= 9:
    for i in range(1, num + 1):
        for j in range(1, i + 1):
            print(i, end=" ")
        print("")
else:
    print("El número debe estar entre 2 y 9")

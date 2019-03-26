'''
Prueba Cubo

@author: Rafael Infante
'''
from Cubo import Cubo

#instancias u objetos
cubito = Cubo(2)
cubote = Cubo(7)

#pinta el cubito 
print("Cubito:  \n")
cubito.pinta()

#pinta el cubote
print("Cubote:  \n")
cubote.pinta()

print("\nLleno el cubito: \n")
cubito.llena()
cubito.pinta()

print("\nEl cubote sigue vacío: \n")
cubote.pinta()

print("\nAhora vuelco lo que tiene el cubito en el cubote.\n")
cubito.vuelcaEn(cubote)

print("Cubito: \n")
cubito.pinta()

print("\nCubote: \n")
cubote.pinta()

print("\nAhora vuelco lo que tiene el cubote en el cubito.\n")
cubote.vuelcaEn(cubito)

print("Cubito: \n")
cubito.pinta()

print("\nCubote: \n")
cubote.pinta()


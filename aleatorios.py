'''
import random

aleat_entero= random.randint(5,245)
print (aleat_entero)

aleat_entero = random.uniform (0.5, 5.0)
print(aleat_entero)
''' 

from random import randint, uniform

aleat_entero= randint(5,245)
print (aleat_entero)

aleat_entero = uniform (0.5, 5.0)
print(aleat_entero)

#crear una lista de 100 numeros aleatorios eneteros
#1. crear una lista vacia

edades = []

#2. generar el numero aleatoreo

edad = randint (0,110)

#3. agregamos el numero a la lista

edades.append(edad)
print(edades)

cont= 0

while cont < 100:
    edad= randint(0,110) 
    edades.append(edad)
    cont= cont + 1
print (edades)

#otro ejemplo
notas = []
for i in range (20):
    print(i)
    nota = uniform(0.0,5.00)
    notas.append(nota)

print(f"Nota = {notas[i]:0.2f}")

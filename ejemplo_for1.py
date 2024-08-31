
# iterar

aviones=['A380', '787','F16', 'Antonov124', 'espiritu san luis']
cont= 1
for avion in aviones:
    print(f'Avion {cont} --> {avion}') 
    cont= cont + 1

# el mismo bucle en while
indice =0
cont= len(aviones) #calcula el numero de elementos de la lista
while indice < cont:
    print (f'avion {indice+1} --> {aviones[indice]}')
    # indice =  indice + 1
    indice +=1

for i in range(5):
    print (f'avion {i+1} --> {aviones[i]}') 

# pedir al usuario que ingrese una frase y contar cuantas 'a' tiene

frase= input("ingrese una frase")
cont=0
for letra in frase:
    if letra =='a':
        cont +=1
print(f"la frase tiene {cont} letras 'a' ")

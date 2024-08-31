lista = [4,54, 66, 77, 32, 11, 12, 34, 34, 56, 7, 5, 3, 6, 77, 44, 2, 2, 45, 78]

acum= 0
n_elem = len(lista)
cont =0
while cont < n_elem:
    acum += lista[cont]
    cont += 1
print(f"la suma es {acum} y debe dar {sum(lista)}") 

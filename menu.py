#menu de operaciones basicas
print("S. Sumar\nR. Restar\nM. Multiplicar\nD. Dividir\nT. Residuo") 
opcion = input("ingrese la opcion deseada")

if opcion not in ["S","R","T","D","M"]:
    print("opcion no valida...!") 

else:
    numero1 = float(input("ingrese el primer valor: "))
    numero2= float(input("ingrese el segundo valor: "))
    if opcion == "S":
       resultado = numero1 + numero2
    elif opcion == "R":
        resultado = numero1 -numero2
    elif opcion == "M":
        resultado = numero1 * numero2
    elif opcion == "D":
        resultado = numero1 / numero2
    elif opcion == "T":
        resultado = numero1 % numero2
    else:
        print(f"resultado es : {resultado}") 

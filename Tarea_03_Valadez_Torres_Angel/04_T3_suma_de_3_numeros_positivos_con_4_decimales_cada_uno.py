#Ejercicio 4: Calculo de suma de numeros positivos con 3 decimales
#Este ejercicio nos pide 3 numeros positivos con 3 decimales cada uno, para calcular la suma de cada uno de ellos y ver cual es el mayor de las sumas resultantes, imprimiendo el resultado con 4 decimales.

def toFixed(value, digits):
    return "%.*f" % (digits, value)

print("Dame el numero n1:")
n1 = float(input())
print("Dame el numero n2:")
n2 = float(input())
print("Dame el numero n3:")
n3 = float(input())
if n1 > 0 and n2 > 0 and n3 > 0:
    ent1 = int(n1)
    dec1 = (n1 - ent1) * 10000
    suma1 = ent1 + dec1
    ent2 = int(n2)
    dec2 = (n2 - ent2) * 10000
    suma2 = ent2 + dec2
    ent3 = int(n3)
    dec3 = (n3 - ent3) * 10000
    suma3 = ent3 + dec3
    print("La suma resultante de n1 = " + toFixed(suma1,4))
    print("La suma resultante de n2 = " + toFixed(suma2,4))
    print("La suma resultante de n3 = " + toFixed(suma3,4))
    if suma1 > suma2:
        if suma1 > suma3:
            mayor = suma1
        else:
            mayor = suma3
    else:
        if suma2 > suma3:
            mayor = suma2
        else:
            mayor = suma3
    print("El valor de las sumas es " + toFixed(mayor,4))
else:
    print("Alguno o varios de los numeros no son positivos")

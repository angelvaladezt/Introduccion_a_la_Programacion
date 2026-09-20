#Angel Valadez Torres 1B
#Ejercicio 1: Calculo de la suma de los divisores de un numero entero positivo
#Documentacion: Este programa pide un numero entero positivo y calcula la suma de todos sus divisores menores o iguales a el, imprimiendo cada divisor y la suma de estos

suma = 0
while True:    
    print("Dame un numero entero positivo: ")
    numero = int(input())
    if numero > 0: 
        break
print("La suma de todos sus divisores menores o iguales a el es:")
for i in range(1, numero + 1, 1):
    if numero % i == 0:
        print(i)
        suma = suma + i
print("Total = " + str(suma))

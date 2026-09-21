#Ejercicio 5. Suma de números impares entre dos enteros positivos
#Documentacion: Este programa solicita 2 números positivos, para calcular la suma de los números impares que se encuentran entre ellos, imprimiendo el resultado sin decimales.

suma = 0
print("Dame el primer número entero positivo: ")
num1 = int(input())
print("Dame el segundo número entero positivo: ")
num2 = int(input())
if num1 < num2:
    menor = num1
    mayor = num2
else:
    menor = num2
    mayor = num1
for i in range(menor, mayor + 1, 1):
    if i % 2 == 1:
        suma = suma + i
print("La suma de los números impares entre los números que me diste es: " + str(suma))

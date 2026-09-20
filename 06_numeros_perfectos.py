#Ejercicio 6: Números perfectos
#Documentacion: Este programa solicita un número entero positivo, para verificar si es perfecto (que es igual a la suma de sus divisores positivos menores a él), imprimiendo el resultado sin decimales.

while True:    #This simulates a Do Loop
    print("Dame un número para verificar si es perfecto: ")
    numero = int(input())
    if numero == 0:
        print("Fin de algoritmo")
    else:
        if numero < 0:
            print("El " + str(numero) + " no es positivo")
        else:
            suma = 0
            for i in range(1, numero - 1 + 1, 1):
                if numero % i == 0:
                    suma = suma + i
            if suma == numero:
                print("El " + str(numero) + " sí es perfecto")
            else:
                print("El " + str(numero) + " no es perfecto")
    if numero == 0: break

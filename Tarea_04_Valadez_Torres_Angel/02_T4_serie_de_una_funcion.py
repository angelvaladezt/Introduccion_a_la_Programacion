#Ejercicio 2: CaLculo de la serie de una funcion
#Documentacion: Este algoritmo nos pide un numero entero positivo y calcula la serie de la funcion f(x) = 2 * f(x-1) + x^2, imprimiendo cada resultado de la funcion.

fx = 0
while True:    #Esto simula un loop de Do
    print("Dame un numero: ")
    numero = int(input())
    if numero > 0: break
print("Segun la funcion, la serie es: ", end='', flush=True) #Para que el resultado quede en la misma linea, se usa end='' y flush=True.
print(str(fx) + " ", end='', flush=True)
for x in range(1, numero + 1, 1):
    fx = (2 * fx) + (x * x)
    print(str(fx) + " ", end='', flush=True)

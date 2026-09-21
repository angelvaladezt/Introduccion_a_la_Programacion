#Ejercicio 4. Serie de Maclaurin para ln(1+x)
#Documentacion: Este programa calcula el valor de ln(1+x) usando la serie de Maclaurin, imprimiendo el resultado con 6 decimales. 
#Proceso hecho por Colin Maclaurin en 1742.

def toFixed(value, digits):
    return "%.*f" % (digits, value)

logaritmo = 0
while True:    #This simulates a Do Loop
    print("Teclee argumento x?")
    x = float(input())
    if x <= -1 or x >= 1:
        print("Error, valor de x inválido")
    if x > -1 and x < 1: break
while True:    #This simulates a Do Loop
    print("Hasta cuantos términos de la serie?")
    n = int(input())
    if n > 0: break
for i in range(1, n + 1, 1):
    termino = ((-1) ** (i - 1)) / i * (x ** i)
    logaritmo = logaritmo + termino
print("ln(1+x) = " + toFixed(float(int(logaritmo * 1000000)) / 1000000,6))

def toFixed(value, digits):
    return "%.*f" % (digits, value)
piMedios = 1.0

while True:
    print("Número de términos? ")
    terminos = int(input())
    if terminos <= 0:
        print("Error, el número debe ser mayor que cero")
    else:
        break

for k in range(1, terminos + 1):
    if k % 2 == 0:
        numerador = k
        denominador = k + 1
    else:
        numerador = k + 1
        denominador = k
    termino = float(numerador) / denominador
    piMedios = piMedios * termino
valorPi = piMedios * 2

if valorPi == int(valorPi):
    print("Valor aproximado de pi = " + str(int(valorPi)))
else:
    print("Valor aproximado de pi = " + toFixed(valorPi, 4))
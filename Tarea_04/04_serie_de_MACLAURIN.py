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

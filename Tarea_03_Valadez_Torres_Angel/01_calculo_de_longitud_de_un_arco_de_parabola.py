#Angel Valadez Torres 1B
# Ejercicio 1: Calcular la longitud del arco de una parabola. (Codigo hecho con la ayuda de Flowgorithm
# Este algoritmo solicita al usuario la altura (H) y el ancho (W) de una parabola y para calcular la longitud del arco (en 4 decimales) usando su formula matematica.

from math import sqrt, log
def toFixed(value, digits):
    return "%.*f" % (digits, value)

print("Ingrese la altura:")
h = float(input())
print("Ingrese el ancho:")
w = float(input())

if h > 0 and w > 0:
    x = h / w
    s = 2 * w * (sqrt(x ** 2 + 1 / 16) + (1 / (16 * x)) * (log(x + sqrt(x ** 2 + 1 / 16)) + log(4)))
    print("La longitud del arco es: " + toFixed(s, 4))
else:
    print("Error: La altura y el ancho deben ser mayores a 0.")
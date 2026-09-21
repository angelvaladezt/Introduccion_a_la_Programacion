#Ejercicio 3: Calculo e impresion del precio de un terreno. (modificado para que quede con los decimales de los ejemplos)
#Este algoritmo pide el largo y ancho de um terreno, y el precio por metro cuadrado, para calcular e imprimir el precio del terreno, aplicando un descuento dependiendo de la cantidad de area del terreno.

print("Ingresa el largo del terreno: ")
largo = float(input())
print("Ingresa el ancho del terreno:")
ancho = float(input())
print("Ingrese precio por metro cuadrado del terreno $: ")
precioM2 = float(input())
area = largo * ancho
if area > 1000:
    descuento = 0.25
else:
    if area > 500:
        descuento = 0.17
    else:
        descuento = 0
precio = (area * precioM2) * (1 - descuento)
texto_precio = f"{precio:.2f}".rstrip('0').rstrip('.')
print("Precio del terreno es: $ ",texto_precio)

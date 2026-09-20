#Ejercicio 5: Tienda departamental
#Este programa pide el monto total de la compra de un usuario, para calcular el descuento que le corresponde y su total a pagar, imprimiendo el resultado con 2 decimales.

print("Monto total de la compra $:")
montoTotal = float(input())
if montoTotal < 500.0:
    descuento = 0
else:
    if montoTotal < 1000.0:
        descuento = 0.05
    else:
        if montoTotal < 7000.0:
            descuento = 0.1
        else:
            if montoTotal < 15000.0:
                descuento = 0.15
            else:
                descuento = 0.25

totalPagar = round(montoTotal - montoTotal * descuento, 2)
if totalPagar == int(totalPagar): # Convertir a entero si el resultado no tiene decimales (para quedar como el ejemplo de $900) 
    totalPagar = int(totalPagar)
print("El total a pagar incluyendo el descuento es $: " + str(totalPagar))

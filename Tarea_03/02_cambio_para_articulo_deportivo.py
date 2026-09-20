#Angel Valadez Torres 1B
#Ejercico 2: Calculo de cambio de un articulo deportivo.
#Este programa pide el costo de un articulo deportivo y el pago del cliente, para calcular el cambio correspondido

print("Dame el costo del articulo deportivo:")
costo = float(input())
print("Dame el pago del cliente:")
pago = float(input())
if pago >= costo:
    cambio = pago - costo
    print("El cambio es: " + str(cambio))
else:
    print("Con esa cantidad no se alcanza a pagar")

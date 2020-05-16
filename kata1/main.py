precio = 3.49
descuento = 1 - 0.6
precio_descuento = precio * descuento 
numero_de_barras = input("introduce el numero de barras")
numero_de_barras = int(numero_de_barras)


print ("precio habitual " + str(precio))
print("descuento " + str(precio_descuento))
print("coste final " + str(numero_de_barras * precio_descuento))

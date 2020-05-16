edad = input("introduce edad")
edad = int(edad)

if edad < 4:
    print("entrada gratis")
elif edad >= 4 and edad < 18:
    print("valor de la entrada: 5 euros")
else:
    print("valor de la entrada: 10 euros")
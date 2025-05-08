# Ejercicio Entrenamiento Python Semana 1 - Modulo 1

#Solicitud de nombre de producto mediante INPUT

nombrep = input("Ingrese el nombre del producto: ")
print(f"Su producto es ✏️: {nombrep}")


#Comprobación de información para la variable PRECIO verificando que la información entregada sea correcta

while True:
    try:
        precioun_str = input("Ingrese el precio unitario en dólares del producto, SOLO en número: ")
        precioun = float(precioun_str)

        if precioun <= 0: #Validación (precio mayor a 0 no puede ser negativo)
            print("Error, el número que ingresaste debe ser positivo, volvete serio, quien pone un numero negativo 😤.")

        else:
            print(f"El nombre del producto es ✏️: {nombrep} y tiene un valor de 💲{precioun} dólares ") #Informacion actual del proceso de la compra
            break  # Sale del bucle si el precio es válido

    except ValueError:
        print("Error: Ingresa un número válido, por favor intenta de nuevo 😡. ") #Si el usuario ingresa un caracter diferente a númerico imprime error

#Comprobación de información para la variable CANTIDAD

while True:
  cantidadp = int(input("Ingrese la cantidad de productos adquiridos: "))

  if cantidadp > 0: #Comprobamos que la cantidad si o si sea mayor a 0 sino repetir el bucle

    print(f"Compraste una cantidad de 🛒: {cantidadp}") #Informacion actual del proceso de la compra

    break

  else:
    print("No ingresaste ninguna cantidad, volve a añadir una cantidad")



haydescuento = input("Tu producto tiene descuento? (Si/No)")

if haydescuento == "si" or haydescuento == "Si" or haydescuento == "sI" or haydescuento == "SI" or haydescuento == "s" or haydescuento == "I"or haydescuento == "S" or haydescuento == "i" or haydescuento == "sii" or haydescuento == "siii": #Funcion para que el usuario ponga cualquier tipo de si
  haydescuento = True

  while True:
    descuentofinal = float(input("Ingrese el descuento sin el % "))

    if 0 <descuentofinal< 100: #Rango de descuento si o si tiene que ser de 0 a 100
      break

    else: print("Ingresa un valor valido")

  #Formula para el descuento

  descuento = (descuentofinal / 100) * precioun
  costo_total = precioun * cantidadp - descuento

  print(f"El total final de la compra CON descuento es de: {costo_total}")#Informacion actual del proceso de la compra
  print(f"📍 Información Compra: \n Producto Nombre ✏️: {nombrep} \n Precio compra💲{precioun} \n Cantidad Productos 🛒: {cantidadp} \n Descuento ✂️: {descuentofinal} \n Total Compra 💲{costo_total} ")

 #Formula sin el descuento
elif haydescuento == "no" or haydescuento == "No" or haydescuento == "nO" or haydescuento == "NO":
  haydescuento = False

  costo_total = precioun * cantidadp

  print(f"El costo final de la compra SIN descuento es de: {costo_total}")
  print(f"📍 Información Compra: \n Producto Nombre ✏️: {nombrep} \n Precio compra💲{precioun} \n Cantidad Productos 🛒: {cantidadp} \n Total Compra 💲{costo_total} ")

else:
  print("Error, solo escriba Si o no")


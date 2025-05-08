print("---------- Bienvenido al programa de gestión de inventario ----------")

inventario = []

def agregar_producto(inventario, nombre, precio, cantidad):
  inventario.append({"nombre": nombre,
                     "precio": precio,
                     "cantidad": cantidad})
  print(f"Su producto ({nombre}) fue añadido al inventario correctamente.")


def buscar_producto(inventario, nombre):
  for producto in inventario:
    if producto["nombre"].lower() == nombre.lower():
       return producto["nombre"], producto["precio"], producto["cantidad"]
  else:
      print(f"Su producto ({nombre}) no fue encontrado en el inventario")
      return None

def actualizar_precio(inventario, nombre, nuevo_precio):
  for producto in inventario:
    if producto["nombre"].lower() == nombre.lower():
      precio_anterior = producto["precio"]
      producto["precio"] = nuevo_precio
      print(f"El precio anterior: ({precio_anterior}) fue actualizado a ({nuevo_precio})")
      return
  print(f"Producto {nombre} no fue encontrado en el inventario.")

def eliminar_producto(inventario, nombre):
  indice_eliminar = -1
  for i, producto in enumerate(inventario):
    if producto["nombre"].lower() == nombre.lower():
      indice_eliminar = i
      break

  if indice_eliminar != -1:
      producto_eliminado = inventario.pop(indice_eliminar)
      print(f"El producto ({producto_eliminado['nombre']}) fue eliminado correctamente.")
  else:
      print(f"El producto ({nombre}) no se encuentra en el inventario.")


def calcular_valor_total(inventario):
  valor_total = sum(producto["precio"] * producto["cantidad"] for producto in inventario)
  return valor_total

def mostrar_inventario(inventario):
  if not inventario:
    print("El inventario está vacío")
    return
  else:
    print("Inventario:")
    for producto in inventario:
      print(f"Nombre: {producto['nombre']}, Precio: ${producto['precio']:.2f}, Cantidad: {producto['cantidad']}")


def menu_usuario():
  while True:
    print("\n゜・:.。..。.:・☆・゜Menú de opciones ☆・゜・:.。..。.:・゜・")
    print("\n Selecciona una opción: ")
    print("\n 1. 🛒 Agregar producto")
    print("\n 2. 🔎 Buscar un producto")
    print("\n 3. 🪄 Actualizar precio de un producto ")
    print("\n 4. 🗑️ Eliminar un producto ")
    print("\n 5. ⚙️ Valor total de inventario ")
    print("\n 6. 📊 Mostrar inventario ")
    print("\n 7. 🛫 Salir")
    print("\n ・:.。..。.:・☆・゜      ☻☻☻         ☆・゜・:.。..。.:・゜・")

    opcion = input("Ingresa la opcion aqui: ")
    return opcion

while True:
  try:
      opcion = menu_usuario()
      match opcion:
          case '1':
              nombre = input("Ingrese el nombre del producto: ")
              precio = float(input("Ingresa el precio del producto: "))
              cantidad = int(input("Ingresa la cantidad del producto: "))
              agregar_producto(inventario, nombre, precio, cantidad)

          case '2':
              nombre = input("Ingresa el nombre del producto a buscar: ")
              resultado = buscar_producto(inventario, nombre)
              if resultado:
                  nombre_prod, precio_prod, cantidad_prod = resultado
                  print(f" 🔎 Su producto es: {nombre_prod}, \n 💲 Su precio es de: ${precio_prod:.2f} \n 🛒 Su cantidad es de: {cantidad_prod}")

          case "3":
              nombre = input("Ingresa el nombre del producto a actualizar: ")
              nuevo_precio = float(input("Ingrese el nuevo precio del producto: "))
              actualizar_precio(inventario, nombre, nuevo_precio)

          case "4":
              nombre = input("Ingresa el nombre del producto a eliminar: ")
              eliminar_producto(inventario, nombre)

          case "5":
              valor_total = calcular_valor_total(inventario)
              print(f"El valor total del inventario es: ${valor_total:.2f}")

          case '6':
              mostrar_inventario(inventario)

          case '7':
              print("Saliendo del programa...")
              print("--------------------------------------")
              break

          case _:
              print("Opción inválida. Por favor, selecciona una opción del menú.")

  except ValueError:
      print("Ingresa un valor válido (numérico) para el precio o la cantidad.")

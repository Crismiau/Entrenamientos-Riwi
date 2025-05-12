print("---------- Bienvenido al programa de gestión de inventario ----------")

inventario = []

def pedir_nombre_producto():
    while True:
        nombre = input("Ingrese el nombre del producto: ").strip()
        if nombre:
            return nombre
        print("⚠️ El nombre del producto no puede estar vacío.")

def pedir_precio():
    while True:
        try:
            precio = float(input("Ingresa el precio del producto: "))
            if precio >= 0:
                return precio
            else:
                print("⚠️ El precio no puede ser negativo.")
        except ValueError:
            print("⚠️ Ingresa un número válido para el precio.")

def pedir_cantidad():
    while True:
        try:
            cantidad = int(input("Ingresa la cantidad del producto: "))
            if cantidad >= 0:
                return cantidad
            else:
                print("⚠️ La cantidad no puede ser negativa.")
        except ValueError:
            print("⚠️ Ingresa un número entero válido para la cantidad.")

def agregar_producto(inventario, nombre, precio, cantidad):
    inventario.append({"nombre": nombre, "precio": precio, "cantidad": cantidad})
    print(f"✅ Producto ({nombre}) añadido correctamente al inventario.")

def buscar_producto(inventario, nombre):
    for producto in inventario:
        if producto["nombre"].lower() == nombre.lower():
            return producto["nombre"], producto["precio"], producto["cantidad"]
    print(f"❌ Producto ({nombre}) no encontrado en el inventario.")
    return None

def actualizar_precio(inventario, nombre, nuevo_precio):
    for producto in inventario:
        if producto["nombre"].lower() == nombre.lower():
            precio_anterior = producto["precio"]
            producto["precio"] = nuevo_precio
            print(f"✅ Precio actualizado de {precio_anterior:.2f} a {nuevo_precio:.2f}")
            return
    print(f"❌ Producto ({nombre}) no encontrado.")

def eliminar_producto(inventario, nombre):
    for i, producto in enumerate(inventario):
        if producto["nombre"].lower() == nombre.lower():
            eliminado = inventario.pop(i)
            print(f"✅ Producto ({eliminado['nombre']}) eliminado del inventario.")
            return
    print(f"❌ Producto ({nombre}) no encontrado para eliminar.")

def calcular_valor_total(inventario):
    return sum(producto["precio"] * producto["cantidad"] for producto in inventario)

def mostrar_inventario(inventario):
    if not inventario:
        print("📦 El inventario está vacío.")
        return
    print("📋 Inventario actual:")
    for producto in inventario:
        print(f"🔸 Nombre: {producto['nombre']}, Precio: ${producto['precio']:.2f}, Cantidad: {producto['cantidad']}")

def menu_usuario():
    print("\n゜・:.。..。.:・☆・゜Menú de opciones ☆・゜・:.。..。.:・゜・")
    print("1. 🛒 Agregar producto")
    print("2. 🔎 Buscar un producto")
    print("3. 🪄 Actualizar precio de un producto")
    print("4. 🗑️ Eliminar un producto")
    print("5. ⚙️ Valor total del inventario")
    print("6. 📊 Mostrar inventario")
    print("7. 🛫 Salir")
    print("・:.。..。.:・☆・゜      ☻☻☻         ☆・゜・:.。..。.:・゜・")
    return input("📌 Ingresa una opción: ")

# Loop principal
while True:
    opcion = menu_usuario()
    match opcion:
        case '1':
            nombre = pedir_nombre_producto()
            precio = pedir_precio()
            cantidad = pedir_cantidad()
            agregar_producto(inventario, nombre, precio, cantidad)

        case '2':
            nombre = pedir_nombre_producto()
            resultado = buscar_producto(inventario, nombre)
            if resultado:
                nombre_prod, precio_prod, cantidad_prod = resultado
                print(f"🔎 Producto: {nombre_prod}\n💲 Precio: ${precio_prod:.2f}\n📦 Cantidad: {cantidad_prod}")

        case '3':
            nombre = pedir_nombre_producto()
            nuevo_precio = pedir_precio()
            actualizar_precio(inventario, nombre, nuevo_precio)

        case '4':
            nombre = pedir_nombre_producto()
            eliminar_producto(inventario, nombre)

        case '5':
            total = calcular_valor_total(inventario)
            print(f"💰 Valor total del inventario: ${total:.2f}")

        case '6':
            mostrar_inventario(inventario)

        case '7':
            print("👋 Saliendo del programa...")
            break

        case _:
            print("⚠️ Opción no válida. Intenta nuevamente.")



#1. Determinar el estado de aprobación:

# Solicita al usuario que ingrese una calificación entre 0 y 100
nota = float(input("Ingresa tu calificación (0/100) aqui: "))

while True:
    try:
        # Verifica que la nota esté en el rango válido (0 a 100)
        if nota >= 0 and nota <= 100:
            # Si la nota es mayor o igual a 60, el estudiante aprueba
            if nota >= 60:
                print(f"Aprobaste tu nota es ({nota})")
                print("")

            else:
                # Si la nota es menor a 60, el estudiante reprueba
                print(f"Reprobaste tu nota es ({nota}) tienes que sacar más de 60 para aprobar.")
                print("")

            break
        else:
            # Si la nota no está en el rango, muestra un mensaje de error
            print("Error tu nota debe ser mayor a 0 y Menor a 100")
            break

    except ValueError:
        # Captura errores si el usuario no ingresa un número válido
        print("Error, ingresa un valor válido")

# 2. Calcular el promedio:

# Solicita al usuario una lista de notas
notas = input("Ingresa la lista de calificaciones separadas con comas ")

# Divide el string en una lista de textos y convierte cada uno a float
calif_texto = notas.split(',')
calificaciones = [float(c) for c in calif_texto]

# Calcula el promedio sumando todas las calificaciones y dividiendo entre la cantidad
promedio = sum(calificaciones) / len(calificaciones)

print(f"El promedio de calificaciones es: {promedio}")
print("")

# 3. Contar calificaciones mayores que un valor específico:

# Solicita al usuario un valor de comparación
valor = float(input("Ingresa una nota mayor para compararla: "))

# Filtra las calificaciones mayores o iguales al valor ingresado
valor_mayor = [c for c in calificaciones if c >= valor]
cant_mayor = len(valor_mayor)

print(f"Hay una cantidad de ({cant_mayor}) notas mayores a {valor}")
print("")
print(f"Estas son las calificaciones mayores o iguales a {valor}: {valor_mayor}")
print("")

# Contar calificaciones menores con un valor específico

# Solicita una nota para comparar calificaciones menores
nota_menor = float(input("Ingresa una nota menor para compararla: "))

# Filtra las calificaciones menores o iguales a la nota ingresada
valor_m = [x for x in calificaciones if x <= nota_menor]
cant_m = len(valor_m)

print(f"Hay una cantidad de ({cant_m}) notas menores a ({nota_menor})")
print("")
print(f"Estas son las calificaciones menores o iguales a {nota_menor}: {valor_m}")
print("")

#4. Verificar y contar calificaciones específicas:

# Solicita una calificación específica a buscar
nota_espc = float(input("Ingresa una calificación especifica: "))


# Cuenta cuántas veces aparece la nota exacta en la lista
nota_igual = calificaciones.count(nota_espc)

valor_igual = [o for o in calificaciones if o == nota_espc]

print(f"Hay una cantidad de ({nota_igual}) notas iguales a {nota_espc}")
print("")
print(f"Las notas iguales son {valor_igual}")

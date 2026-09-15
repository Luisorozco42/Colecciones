# Son una colección similar a las listas. (Tuple en inglés)
# Estas son inmutables, por lo tanto, no se puede modificar el tamaño, ni agregar o eliminar datos.
# Estos se suelen usar para crear colecciones de datos que no deben cambiar con el tiempo.

print("*** Manejo de Tuplas ***")

mi_tupla = (1,2,3,4,5)
print(mi_tupla)
# Recordando el hecho de que no se puede agregar o eliminar, al poner . no salen muchos de los metodos que otras colecciones nos ofrecen

for elemento in mi_tupla:
    print(elemento, end=" ")

# Crear una tupla para una coordenada x, y
coordenadas = (3, 5)
# Accedemos a cada elemento de la tupla
print(f"\nCoordenada en el eje x: {coordenadas[0]}")
print(f"Coordenada en el eje y: {coordenadas[1]}")

# Se pueden crear tuplas unitarias
tupla_un_elemento = 10, # la coma señala que es una tupla
print(f"Tupla de un elemento: {tupla_un_elemento}")

# Tupla anidada (xd, si las listas se anidan, por k las tuplas no verdad?
tupla_anidada = (1, (2,3), (4,5))

print(f"Tupla anidada: {tupla_anidada[1]}")

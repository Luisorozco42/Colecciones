# iniciamos con listas
print("*** Manejo de Listas ***")

mi_lista = [1, 2, 3, 4, 5]
print(f'{mi_lista} -> Lista original')

# largo de una lista
print(f"Largo de la lista: {len(mi_lista)}")

# Acceder a los elementos de la lista por indice
print(f"Accedemos al valor del indice 4: {mi_lista[4]}")
print(f"Accedemos al último indics de la lista: {mi_lista[-1]}")

# Modificar elementos de una lista
mi_lista[1] = 10

print(f"Modificamos el valor del índice 1: {mi_lista[1]}")

# Agregar un nuevo elemento al final de la lista
mi_lista.append(6)

print(f"{mi_lista} -> Se agregó el elemento 6")

#Añadir un nuevo elemento en un índice específico
mi_lista.insert(2,15) # insert(índice, valor)

print(f"{mi_lista} -> se agrego el valor de 15 en el índice 2")

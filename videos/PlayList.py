print("*** Playlist de Canciones ***")

lista_reproduccion = []

numero_canciones = int(input("Cuantas canciones deseas agregar?\n"))

for indice in range(numero_canciones):
    cancion = input(f"Proporciona la canción {indice + 1}: ")
    lista_reproduccion.append(cancion)

# Ordenar la lista en orden alfabético. sort
lista_reproduccion.sort()
# lista_reproduccion.sort(reverse=True) para orden al revés

# Mostrar la lista de canciones
print(f"\nLista de Reproducción en orden alfabético:")
print(lista_reproduccion)

# Mostrando la lista iterando sus elementos
print("Iteramos el playlist")
for cancion in lista_reproduccion:
    print(f"- {cancion}")

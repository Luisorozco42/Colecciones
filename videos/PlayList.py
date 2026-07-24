print("*** Playlist de Canciones ***")

lista_reproduccion = []

lista_reproduccion.append('Hotel California - Eagles')
lista_reproduccion.append('Staying Alive - Bee Gees')
lista_reproduccion.append('Dream on - Aerosmith')

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

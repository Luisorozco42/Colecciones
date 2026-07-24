print("*** Promedio de Calificaciones ***")

cant_calificaciones = int(input("Proporciona el no. de calificaciones a evaluar: "))
calificaciones = []
total_calificaciones = 0.00
promedio_calificaciones = 0.00

for indice in range(cant_calificaciones):
    calificacion = float(input(f"Calificación[{indice}] = "))
    calificaciones.append(calificacion)

for indice in range(cant_calificaciones):
    total_calificaciones += calificaciones[indice]

promedio_calificaciones = total_calificaciones / cant_calificaciones

print(f"Las calificaciones proporcionadas son: {calificaciones}")
print(f"Promedio de las Calificaciones: {promedio_calificaciones}")

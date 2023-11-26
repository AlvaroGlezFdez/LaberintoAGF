muro = ((0,1), (0,2), (0,3), (0,4), (1,1), (2,1), (2,3), (3,3), (4,0), (4,1), (4,2), (4,3))

# Establecemos las dimensiones del laberinto
filas = 5
columnas = 5

laberinto = [[" "for _ in range(columnas)] for _ in range(filas)]

for coordenadas in muro:
    fila,columna = coordenadas
    laberinto[fila][columna] = "X"

for fila in laberinto:
    print(" ".join(fila))
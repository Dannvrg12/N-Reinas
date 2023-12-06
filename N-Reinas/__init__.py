def es_seguro(tablero, fila, columna):
    for i in range(fila):
        if tablero[i] == columna or \
           tablero[i] - i == columna - fila or \
           tablero[i] + i == columna + fila:
            return False
    return True

#Si tablero[i] == columna, significa que hay una reina en la misma columna.
#tablero[i] - i: Representa la posición de la reina en la diagonal superior izquierda.Cuando tablero[i] - i == columna - fila, significa que hay una reina en la misma diagonal.
#tablero[i] + i: Representa la posición de la reina en la diagonal superior derecha.Cuando tablero[i] + i == columna + fila, significa que hay una reina en la misma diagonal.


def resolver_n_reinas(n):
    tablero = [-1] * n
    return resolver_n_reinas_util(tablero, 0, n)

 #Esta función es la función principal que inicializa el tablero y llama a la función resolver_n_reinas_util con los parámetros iniciales.
 #Se inicializa una lista llamada tablero con valores -1, indicando que inicialmente no hay reinas colocadas en el tablero.   
 #La función llama a resolver_n_reinas_util con el tablero inicializado, comenzando desde la fila 0 y especificando el tamaño del tablero.
 #La función retorna el resultado de la llamada a resolver_n_reinas_util, que es una lista de todas las soluciones encontradas.

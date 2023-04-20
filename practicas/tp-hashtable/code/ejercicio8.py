def kmp_search(text, pattern):
    n = len(text)
    m = len(pattern)
    f = [0] * m  # Inicializamos la tabla de fallos
    
    # Construimos la tabla de fallos
    j = 0
    for i in range(1, m):
        while j > 0 and pattern[i] != pattern[j]:
            j = f[j-1]
        if pattern[i] == pattern[j]:
            j += 1
        f[i] = j
    
    # Realizamos la búsqueda del patrón en el texto
    i = 0
    j = 0
    while i < n and j < m:
        if text[i] == pattern[j]:
            i += 1
            j += 1
        elif j > 0:
            j = f[j-1]
        else:
            i += 1
    if j == m:
        return i - j  # Devolvemos el índice de la primera ocurrencia
    else:
        return -1  # No se encontró ninguna ocurrencia del patrón
def mostrarTablas(llaves,m):
  print('Linear Probing')
  print(hash_linear_probing(llaves,m))
  print('Quadratic Probing')
  print(hash_quadratic_probing(llaves,m))
  print('Double hashing Probing')
  print(hash_double_hashing(llaves,m))



def hash_linear_probing(llaves, m):
  tabla = [None] * m
  for llave in llaves:
    i = llave % m
    while tabla[i] is not None:
      i = (i + 1) % m
    tabla[i] = llave
  return tabla


def hash_double_hashing(llaves, m):
  tabla = [None] * m
  for llave in llaves:
    i = llave % m
    j = 1 + (llave % (m - 1))
    while tabla[i] is not None:
      j += 1
      i = (i + j) % m
    tabla[i] = llave
  return tabla


def hash_quadratic_probing(llaves, m):
  tabla = [None] * m
  c1 = 1
  c2 = 3
  for llave in llaves:
    i = llave % m
    j = 0
    while tabla[i] is not None:
      j += 1
      i = (llave + c1*j + c2*j**2) % m
    tabla[i] = llave
  return tabla


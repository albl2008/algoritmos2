def hash_codigo_postal(codigo_postal):
  hash_value = 0
  for c in codigo_postal:
    if c.isdigit():
      hash_value += ord(c) - ord('0')
    else:
      hash_value += ord(c) - ord('A') + 10
  return hash_value

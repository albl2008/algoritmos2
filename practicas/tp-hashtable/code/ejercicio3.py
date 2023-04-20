import math
keys = [61,62,63,64,65]

A = (math.sqrt(5) - 1)/2

def hash(k,A):
  m=1000
  val = k * A % 1

  h = math.floor(m*val)

  return h

def printIndex():
  for k in keys:
    print(hash(k,A))
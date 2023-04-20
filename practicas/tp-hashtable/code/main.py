from dictionary import *
from ejercicio8 import kmp_search
from ejercicio3 import printIndex
from ejercicio4 import isPermutation
from ejercicio5 import checkUnique
from ejercicio7 import compressStr
from ejercicio9 import isSubSet
from ejercicio10 import mostrarTablas

dict = [None] * 10

insert(dict, 5, 'Hola')
insert(dict, 28, 'Pedro')
insert(dict, 19, 'Como')
insert(dict, 15, 'Te')
insert(dict, 20, 'Va')

delete(dict, 20)
print(search(dict, 15))
traverseHashTable(dict)
print(kmp_search('abracadabra', 'aca'))

printIndex()

L = [1, 5, 12, 15, 2]

print(checkUnique(L))

print(isPermutation('hola', 'olag'))

print(compressStr('aaaabddcccccaa'))

S = [1, 3, 4, 6, 8]
T = [3, 6, 9]

print(isSubSet(S, T))

llaves = [10,22,31,4,15,28,17,88,59]
m=11
mostrarTablas(llaves,m)

m=10
L = [42, 46, 33, 23, 34, 52]
def hash(k):
  index = k % 10
  return index

for i in range (6):
  print(hash(L[i]))
  
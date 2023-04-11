from classes import *
from trie import *


T = Trie()
T.root = TrieNode()

insert(T,'hola')
insert(T,'holanda')
insert(T,'aloh')
insert(T,'pepe')

T2= Trie()
T2.root = TrieNode()

insert(T2,'hola')
insert(T2,'holanda')
insert(T2,'aloh')


#print('Identical trie: ',checkIdenticalTrie(T,T2))
#print(search(T,'pepe'))
#print(search(T,'hola'))

insert(T,'pepito')

#delete(T,'hola')
#print(search(T,'hola'))

#print('Chequeo cadena invertida:', checkInvertedString(T))
print('Autocompletar pepi')
print(autoCompletar(T,'pepi'))


print(printWithLenN(T,'ho',7))


words = []
words2 = []
print('T1: ',traverse(T.root, "", words))
print('T2: ',traverse(T2.root, "", words2))

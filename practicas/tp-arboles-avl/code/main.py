from classes import *
from avltree import *
from avltree import *

B = AVLTree()


print(insert(B,'A',29))
print(insert(B,'B',20))
print(insert(B,'C',40))
print(insert(B,'D',15))
print(insert(B,'E',25))
print(insert(B,'F',32))
print(insert(B,'G',50))
print(insert(B,'H',10))
print(insert(B,'I',17))
print(insert(B,'J',21))
print(insert(B,'K',26))
print(insert(B,'L',30))
print(insert(B,'M',35))
print(insert(B,'N',47))
print(insert(B,'O',55))

calculateBalance(B)

L = traversePreOrder(B)
print('PreOrden de Balance Factor')
printList(L)

LL = traversePreOrden(B)
print('PreOrden de Values')
printList(LL)


AVL = AVLTree()

print(insertAVL(AVL,'A',29))
print(insertAVL(AVL,'B',30))
print(insertAVL(AVL,'C',40))
print(insertAVL(AVL,'D',45))
print(insertAVL(AVL,'E',55))
print(insertAVL(AVL,'F',62))
print(insertAVL(AVL,'H',64))

calculateBalance(AVL)

avlL = traversePreOrder(AVL)
print('PreOrden de BF')
printList(avlL)

avlV = traversePreOrden(AVL)
print('PreOrden de Values')
printList(avlV)

deleteKey(AVL,55)

avlL = traversePreOrder(AVL)
print('PreOrden de BF')
printList(avlL)

avlV = traversePreOrden(AVL)
print('PreOrden de Values')
printList(avlV)



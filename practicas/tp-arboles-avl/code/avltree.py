from linkedlist import add, printList
from classes import *


def rotateLeft(Tree, avlnode):
  if avlnode and avlnode.rightnode:
    newRoot = avlnode.rightnode
    avlnode.rightnode = newRoot.leftnode

    if newRoot.leftnode != None:
      newRoot.leftnode.parent = avlnode
    newRoot.parent = avlnode.parent

    if avlnode.parent == None:
      Tree.root = newRoot
    else:
      if avlnode.parent.leftnode == avlnode:
        avlnode.parent.leftnode = newRoot
      else:
        avlnode.parent.rightnode = newRoot

    newRoot.leftnode = avlnode
    avlnode.parent = newRoot


def rotateRight(Tree, avlnode):
  if avlnode and avlnode.leftnode:
    newRoot = avlnode.leftnode
    avlnode.leftnode = newRoot.rightnode

    if newRoot.rightnode != None:
      newRoot.rightnode.parent = avlnode
    newRoot.parent = avlnode.parent

    if avlnode.parent == None:
      Tree.root = newRoot
    else:
      if avlnode.parent.rightnode == avlnode:
        avlnode.parent.rightnode = newRoot
      else:
        avlnode.parent.leftnode = newRoot

    newRoot.rightnode = avlnode
    avlnode.parent = newRoot


def height(root):
  if root == None:
    return -1

  lh = height(root.leftnode)
  rh = height(root.rightnode)

  return max(lh, rh) + 1


def calculateBalance(AVLTree):
  calculateBf(AVLTree.root)
  return AVLTree


def calculateBf(root):
  left = height(root.leftnode)
  right = height(root.rightnode)
  root.bf = left - right
  if root.leftnode != None:
    calculateBf(root.leftnode)
  if root.rightnode != None:
    calculateBf(root.rightnode)


def insert(B, element, key):
  root = B.root
  newNode = AVLNode()
  newNode.value = element
  newNode.key = key
  if root == None:
    B.root = newNode
    return key
  else:
    newKey = insertNode(newNode, root)
    return newKey


def insertAVL(B, element, key):
  root = B.root
  newNode = AVLNode()
  newNode.value = element
  newNode.key = key
  if root == None:
    B.root = newNode
    return key
  else:
    newKey = insertNode(newNode, root)
  reBalance(B)
  return newKey


def insertNode(newNode, current):
  if newNode.key < current.key:
    if current.leftnode == None:
      current.leftnode = newNode
      newNode.parent = current
    else:
      insertNode(newNode, current.leftnode)
  elif newNode.key > current.key:
    if current.rightnode == None:
      current.rightnode = newNode
      newNode.parent = current
    else:
      insertNode(newNode, current.rightnode)

  if newNode.parent != None:
    return newNode.key
  else:
    return None


def nodeByKey(key, root):
  current = root
  if current == None:
    return None
  elif current.key == key:
    return current
  else:
    if nodeByKey(key, current.rightnode):
      return nodeByKey(key, current.rightnode)
    else:
      return nodeByKey(key, current.leftnode)


def deleteKey(B, key):
  if B.root == None:
    return None
  else:
    key = delKey(B.root, key)
    reBalance(B)
  return key


def delKey(root, key):
  if root != None:
    if root.key == key:
      if root.rightnode == None and root.leftnode == None:
        parent = root.parent
        if parent.key > key:
          parent.leftnode = None
        else:
          parent.rightnode = None
        return key

      elif root.rightnode == None and root.leftnode != None:
        parent = root.parent
        root.leftnode.parent = parent
        if key < parent.key:
          parent.leftnode = root.leftnode
        else:
          parent.rightnode = root.leftnode
        return key

      elif root.rightnode != None and root.leftnode == None:
        parent = root.parent
        root.rightnode.parent = parent
        if key < parent.key:
          parent.leftnode = root.rightnode
        else:
          parent.rightnode = root.rightnode
        return key

      else:
        successornode = inorderSucessor(root)
        root.value = successornode.value
        root.key = successornode.key

        if root.leftnode == successornode:
          root.leftnode = None
        else:
          delKey(root.leftnode, successornode.key)
        return key

    elif root.key < key:
      return delKey(root.rightnode, key)
    else:
      return delKey(root.leftnode, key)


def inorderSucessor(N):
  if isLeaf(N):
    parentNode = N.parent
    while parentNode.key < N.key:
      parentNode = parentNode.parent
    return parentNode
  N = N.rightnode
  if N:
    return successorNode(N)
  else:
    return None


def successorNode(node):
  if node.leftnode == None:
    return node
  else:
    return successorNode(node.leftnode)


def isLeaf(node):
  if node.leftnode == None and node.rightnode == None:
    return True
  else:
    return False


def reBalance(AVLTree):
  calculateBalance(AVLTree)
  reBalanceTree(AVLTree, AVLTree.root)


def reBalanceTree(Tree, root):
  if root.bf < 0:
    if root.rightnode.bf > 0:
      rotateRight(Tree, root.rightnode)
      rotateLeft(Tree, root)
    else:
      rotateLeft(Tree, root.rightnode)
  elif root.bf > 0:
    if root.leftnode.bf < 0:
      rotateLeft(Tree, root.leftnode)
      rotateRight(Tree, root)
    else:
      rotateRight(Tree, root.leftnode)


def preOrder(current, L):
  if current != None:
    add(L, current.bf)
    preOrder(current.leftnode, L)
    preOrder(current.rightnode, L)
  return L


def preOrden(current, L):
  if current != None:
    add(L, current.value)
    preOrden(current.leftnode, L)
    preOrden(current.rightnode, L)
  return L


def traversePreOrder(B):
  root = B.root
  preOrderList = LinkedList()
  preOrderList = preOrder(root, preOrderList)
  return preOrderList


def traversePreOrden(B):
  root = B.root
  preOrderList = LinkedList()
  preOrderList = preOrden(root, preOrderList)
  return preOrderList

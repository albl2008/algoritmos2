from classes import *


def add(L, element):
    current = L.head
    node = Node()
    node.value = element
    if current == None:
        L.head = node
    else:
        node.nextNode = current
        L.head = node


def search(L, element):
    current = L.head
    pos = 0
    while current != None:
        if current.value == element:
            return pos
        current = current.nextNode
        pos += 1
    return None


def insert(L, element, position):
    if position > length(L):
        return None
    elif position == 0:
        add(L, element)
        return position
    else:
        current = L.head
        index = 0
        while current != None and index < position - 1:
            current = current.nextNode
            index += 1
        node = Node()
        node.value = element
        if current != None:
            node.nextNode = current.nextNode
            current.nextNode = node
            return position

def delete(L,element):
  pos = search(L,element)
  
  if pos == None:
    return None
  elif pos >= 1:
    current = L.head
    index = 0
    while index<pos:
      aux = current
      current = current.nextNode
      index += 1
    aux.nextNode = current.nextNode
    return pos
  else:
    current = L.head
    L.head = current.nextNode
    return pos


def access(L,position):
  if position > length(L):
    return None
  else:
    current = L.head
    index = 0
    while current != None and index < position:
      current = current.nextNode
      index += 1
    return current.value

def update(L,element,position):
  if position > length(L):
    return None
  else:
    current = L.head
    index = 0
    while current != None and index < position:
      current = current.nextNode
      index += 1
    current.value = element
    return position
      
        
    
  

def length(L):
    current = L.head
    len = 0
    while current != None:
        current = current.nextNode
        len += 1
    return len


def printList(L):
  if L:
    current = L.head
    if current == None:
      print('Lista sin elementos')
    else:  
      print('LISTA: ')
      while current != None:
        print(current.value, end=" ")
        current = current.nextNode
      print(' ')
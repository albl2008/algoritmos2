def hash_function(key, m):
    return key % m 

def insert(D, key, value):
    index = hash_function(key, len(D))
    if D[index] is None:
        D[index] = [(key, value)]
    else:
        for i, (k, v) in enumerate(D[index]):
            if k == key:
                D[index][i] = (key, value)
                break
        else:
            D[index].append((key, value))
    return D

def search(D, key):
    m = len(D)
    idx = hash_function(key, m)
    for k, v in D[idx]:
        if k == key:
            return v  
    return None  

def delete(D, key):
    m = len(D)
    idx = hash_function(key, m)
    for i, (k, v) in enumerate(D[idx]):
        if k == key:
            del D[idx][i]  
            return D
    return D  


def traverseHashTable(D):
  size = len(D)
  for i in range (size):
    print('Index: ',i)
    if D[i]!=None:
      for key,value in D[i]:
        print('Key: ',key, 'Value: ', value)
    else:
      print(None)
  
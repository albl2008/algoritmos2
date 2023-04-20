def checkUnique(L):
  elements = []
  for value in L:
    if value in elements:
      return False
    elements.append(value)
  return True
    
      
  
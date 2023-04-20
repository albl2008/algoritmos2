def isPermutation(s,p):
  char_count = {}
  for c in s:
    if c in char_count:
      char_count[c] += 1
    else:
      char_count[c] = 1
  for c in p:
    if c not in char_count or char_count[c] == 0:
      return False
    char_count[c] -= 1

  
  return True
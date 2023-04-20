def isSubSet(S,T):
  if len(T)>len(S):
    return False
  else:
    dict = {}
    for t in T:
      dict[t] = t

    for s in S:
      if s not in dict:
        return False
    return True
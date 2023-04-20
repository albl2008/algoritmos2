def compressStr(s):
  compress = ''
  cont = 0 

  for i in range(len(s)-1):
    if s[i] == s[i+1]:
      if i == 0 :
        cont += 2
      else:
        cont += 1
    else:
      compress += s[i] + str(cont)
      cont = 1
  compress += s[-1] + str(cont)
  if len(compress)>len(s):
    return s
  else:
    return compress
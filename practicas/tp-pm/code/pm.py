def existChar(string, c):
  for char in string:
    if char == c:
      return True
  return False


def isPalindrome(string):
  string = string.lower()
  return string == string[::-1]


def mostRepeatedChar(string):
  char_count = {}

  for char in string:
    if char in char_count:
      char_count[char] += 1
    else:
      char_count[char] = 1

  max_count = 0
  most_repeated_char = None
  for char, count in char_count.items():
    if count > max_count:
      max_count = count
      most_repeated_char = char

  return most_repeated_char


def verifyBalancedParentheses(s):
  stack = []
  for char in s:
    if char == '(':
      stack.append(char)
    elif char == ')':
      if len(stack) == 0 or stack[-1] != '(':
        return False
      stack.pop()
  return len(stack) == 0


def reduceLen(string):
  stack = []

  for char in string:
    if stack and stack[-1] == char:
      stack.pop()
    else:
      stack.append(char)
  return ''.join(stack)


def isContained(s, word):
  s_index = 0
  word_index = 0

  while s_index < len(s) and word_index < len(word):
    if s[s_index] == word[word_index]:
      word_index += 1
    s_index += 1

  return word_index == len(word)


def kmp_search(text, pattern):
  n = len(text)
  m = len(pattern)
  f = [0] * m  # Inicializamos la tabla de fallos

  # Construimos la tabla de fallos
  j = 0
  for i in range(1, m):
    while j > 0 and pattern[i] != pattern[j]:
      j = f[j - 1]
    if pattern[i] == pattern[j]:
      j += 1
    f[i] = j

  # Realizamos la búsqueda del patrón en el texto
  i = 0
  j = 0

  while i < n:
    while i < n and j < m:
      if text[i] == pattern[j]:
        i += 1
        j += 1
      elif j > 0:
        j = f[j - 1]
      else:
        i += 1
    if j == m:
      return i - j  # Devolvemos el índice de la primera ocurrencia
    else:
      return -1  # No se encontró ninguna ocurrencia del patrón


def KMP(s1, s2):
  i = kmp_search(s1, s2)
  if i == -1:
    return None
  end = i + len(s2)
  occurrences = []

  for j in range(i, end):
    occurrences.append(j)

  return occurrences

def findPrefix(T, P):
    i = 0
    j = 0
    
    while i < len(T) and j < len(P):
        if T[i] == P[j]:
            i += 1
            j += 1
        else:
            break
    
    return T[:i]

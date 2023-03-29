
def contiene_suma(A, n):
    A.sort()
    i = 0
    j = len(A) - 1
    while i < j:
        if A[i] + A[j] == n:
            return True
        elif A[i] + A[j] < n:
            i += 1
        else:
            j -= 1
    return False



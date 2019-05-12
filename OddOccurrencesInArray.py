def solution(A):
    if len(A) == 1:
        return A[0]
    A = sorted(A)

    i = 0
    while i < len(A):
        try:
            if A[i] == A[i + 1]:
                i += 2
            else:
                return A[i]
        except:
            return A[len(A) - 1]
    pass

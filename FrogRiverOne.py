def solution(X, A):
    a = list(range(0, X))
    for idx, val in enumerate(A):
        if val in a:
            a.remove(val)
        if len(a) == 0:
            return idx

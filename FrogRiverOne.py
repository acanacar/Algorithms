def solution(X, A):
    a = list(range(0, X))
    for id, val in enumerate(A):
        if val in a:
            a.remove(val)
        if len(a) == 0:
            return id

def solution(A):
    N = len(A)
    partFirst = A[0]
    partSecond = sum(A[1:])
    mindif = abs(partFirst - partSecond)
    for p in range(1, N - 2):
        partFirst += A[p]
        partSecond -= A[p]
        result = abs(partFirst - partSecond)
        if result < mindif:
            mindif = result
        else:
            continue
    return mindif

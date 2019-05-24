def solution(A):
    l = [False] * (len(A) + 1)
    for i in A:
        if 0 < i <= len(A):
            l[i - 1] = True
    for ind, val in enumerate(l):
        if not val:
            return ind + 1

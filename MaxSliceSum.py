def solution(A):
    max_slice = max_current = - 1000000
    for i in A:
        max_current = max(i, i + max_current)
        max_slice = max(max_current, max_slice)
    return max_slice

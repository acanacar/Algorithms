def solution(A):
    if len(A) == len(set(A)):
        if (max(A) * max(A) + 1) == 2 * sum(A):
            return 1
        else:
            return 0
    else:
        return 0

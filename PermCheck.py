def solution(A):
    if len(A) == len(set(A)):
        if (max(A) * max(A) + 1) == 2 * sum(A):
            return 1
        else:
            return 0
    else:
        return 0


def AlternativeSolution(A):
    l = len(A)
    checkarray = [False] * l

    for i in A:
        if 0 <= i > l:
            return 0
        if checkarray[i - 1] == True:
            return 0
        checkarray[i - 1] = True

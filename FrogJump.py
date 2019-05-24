def AlternativeSolution(X, Y, D):
    if X == Y:
        return 0
    i = 1
    while X < Y:
        X = X + D * i
        i += 1
    return i

import math
def solution(X, Y, D):
    a = Y - X
    if a == 0:
        return 0
    else:
        return math.ceil(a/D)

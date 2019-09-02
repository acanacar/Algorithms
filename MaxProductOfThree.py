def solution(A):
    if len(A) < 3 or len(A) > 100000:
        raise Exception("invalid input")
    A.sort()

    return max(A[-1]*A[0] * A[1] , A[-1] * A[-2] * A[-3])


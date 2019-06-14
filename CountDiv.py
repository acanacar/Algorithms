def solution(A, B, K):
    if B < A or K <= 0:
        raise Exception("Invalid Input")
    min_value_divisible = A + A % K
    if min_value_divisible > B:
        return 0
    return ((B - min_value_divisible) // K) + 1

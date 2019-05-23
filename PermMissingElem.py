def solution(A):
    n = len(A)
    sum_Without_Missing = int((n + 1) * (n + 2) / 2)
    sum_With_Missing = sum(A)
    print("sum_Without_Missing => ", sum_Without_Missing)
    print("sum_With_Missing => ", sum_With_Missing)
    return sum_Without_Missing - sum_With_Missing

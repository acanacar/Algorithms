from itertools import combinations


def solution(A):
    A.sort()
    items = list(combinations(A, 3))
    for item_1, item_2, item_3 in items:
        if item_1 + item_2 > item_3 and item_1 + item_3 > item_2 and item_2 + item_3 > item_1:
            return 1
        else:
            return 0

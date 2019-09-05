from collections import Counter


def solution(A):
    item, count = Counter(A).most_common(1)[0]
    if not count > (len(A) / 2):
        return -1
    else:
        return A.index(item)

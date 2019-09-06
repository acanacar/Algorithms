from collections import Counter


def solution(A):
    item, count = Counter(A).most_common()[0]
    if not count > (len(A) / 2):
        return 0

    left_cnt = 0
    equi_cnt = 0
    for idx, ele in enumerate(A):
        if ele == item:
            left_cnt += 1
        if left_cnt > (idx + 1) // 2 and count - left_cnt > (len(A) - idx - 1) // 2:
            equi_cnt += 1

    return equi_cnt

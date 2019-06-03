def solution(A):
    countWest = 0
    countTotalPairs = 0

    for i in A:
        if i == 1:
            countTotalPairs += countWest
        else:
            countWest += 1

    if countTotalPairs > 10 ** 9:
        return -1
    return countTotalPairs

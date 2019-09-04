def solution(S):
    if len(S) == 0:
        return 1
    left_paranthesis = 0
    for ele in S:
        if ele == '(':
            left_paranthesis += 1
        else:
            if left_paranthesis == 0:
                return 0
            left_paranthesis -= 1

    if left_paranthesis != 0:
        return 0

    return 1

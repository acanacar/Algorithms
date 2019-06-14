def solution(S, P, Q):
    l = {'A': 1, 'C': 2, 'G': 3, 'T': 4}
    result = []
    for i in range(len(P)):
        start_ind, end_ind = P[i], Q[i]
        val = min(list(map(lambda x: l[x], S[start_ind:end_ind + 1])))
        result.append(val)
    return result

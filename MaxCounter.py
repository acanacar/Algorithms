def solution(N, A):
    la = [0] * N
    for i in A:
        if i == N + 1:
            la = [max(la)] * N
        else:
            la[i - 1] += 1
    return la

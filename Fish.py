def Solution(A, B):
    alive, stack = 0, []

    for ind in range(len(A)):
        if B[ind] == 0:
            while len(stack) != 0:
                if stack[-1] > A[ind]:
                    break
                else:
                    stack.pop()
            else:
                alive += 1
        else:
            stack.append(A[ind])
    return alive + len(stack)

def isvalid(stacklast, element):
    if stacklast == '[' and element == ']':
        return True
    if stacklast == '(' and element == ')':
        return True
    if stacklast == '{' and element == '}':
        return True
    return False


def solution(S):
    stack = []
    for element in S:
        if element == '[' or element == '(' or element == '{':
            stack.append(element)
        else:
            if len(stack) != 0:
                last = stack.pop()
                if not isvalid(last, element):
                    return False

    if len(stack) != 0:
        return False
    return True

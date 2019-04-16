# [1,2,3,4,5,6]  -->  123456123456123456|=>123456<=|123456123456123456
# the number between arrows are our exact list

def rotate(L, R):
    # 2=> 651234
    # 3=>456123
    if len(L) > 0:
        result = L[-R:] + L[:-R]
    else:
        result = L

    return result

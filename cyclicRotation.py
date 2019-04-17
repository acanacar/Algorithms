# [1,2,3,4,5,6]  -->  123456123456123456|=>123456<=|123456123456123456
# the number between arrows are our exact list

def rotate(L, R):
    # 2=> 651234
    # 3=>456123
    R = R % len(L)
    if len(L) == 0 or R == 0:
        return L
    else:
        return L[-R:] + L[:-R]


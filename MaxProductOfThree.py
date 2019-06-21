def solution(A):
    if len(A)<3 or len(A)>100000:
        raise Exception("invalid input")
    A.sort()
    if A[0]>1000 or A[-1]<-1000:
        raise Exception("invalid item")

    if A[0]>0:
        return A[-1]*A[-2]*A[-3]
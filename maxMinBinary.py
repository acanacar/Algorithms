def decimalToBinary(n):
    return bin(n).replace("0b", "")


def findMax(X):
    arrBin = decimalToBinary(X)
    l = [i for i, n in enumerate(arrBin) if n == '1']
    k = []
    for i in range(len(l) - 1):
        dif = l[i + 1] - l[i] - 1
        k.append(dif)
    print('l: ', l)
    print('k: ', k)
    return max(k)


print(findMax(15))

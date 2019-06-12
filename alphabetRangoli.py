def solution(n):
    width = 4 * n - 3
    upheight, downheight = n - 1, n - 1
    items = [chr(97+i) for i in range(n)]
    lstart = items[1:]
    lstart.reverse()
    l = lstart + items
    storeOfUpLines = []
    for rowIndex in range(upheight+1):
        elementsToUse = l[:rowIndex+1]
        startPart = elementsToUse[:-1]
        endPart = elementsToUse[:-1]
        endPart.reverse()
        centerElement = elementsToUse[-1:]
        text = startPart + centerElement + endPart
        text = '-'.join(map(str,text))
        storeOfUpLines.append(text)
        print(text.center(width,'-'))

    storeOfUpLines.reverse()
    for text in storeOfUpLines[1:]:
        print(text.center(width,'-'))

def getAlternates (arr):
    res = []

    for i in range(0,len(arr),2):
        res.append(arr[i])
    return res

arr = [10,20,30,40,50]
res = getAlternates(arr)
print(res)
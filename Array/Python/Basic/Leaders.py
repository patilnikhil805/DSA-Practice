def leaders(arr):
    result = []
    n = len(arr)

    maxRight = arr[-1]

    result.append(maxRight)

    for i in range(n-2, -1, -1):
        if arr[i] > maxRight:
            maxRight = arr[i]
            result.append(maxRight)

    result.reverse()

    return result

arr = [12,413,134,135,123,335,2135]
result = leaders(arr)
print(result)
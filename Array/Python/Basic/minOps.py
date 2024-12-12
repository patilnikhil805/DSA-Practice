def minOps(arr, n, k):
    max1 = max(arr)
    n = len(arr)
    res = 0 

    for i in range(0,n):
        if ((max1 - arr[i]) % k != 0):
            return -1
        
        else:
            res += (max1 - arr[i]) / k 

    return int(res)


arr = [21, 33, 9, 45, 63] 
n = len(arr)
k = 6
print(minOps(arr, n, k))
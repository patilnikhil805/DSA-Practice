def search(arr,N,x):
    for i in range(0,N):
        if (arr[i] == x):
            return i
    return -1

arr=[10,20,30,40,50]
x = 5
N = len(arr)

result = search(arr, N, x)
print(result)

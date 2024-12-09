def removeDuplicates(arr):
    n = len(arr)
    if n <= 1:
        return n
    
    index = 1
    for i in range(1, n):
        if arr[i] != arr[i - 1]:
            arr[index] = arr[i]
            index += 1
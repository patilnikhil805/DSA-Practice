def selection(arr):

    n = len(arr)
    for i in range(n):
        min_index = i

        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        
        arr[iS]
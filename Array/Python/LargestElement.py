def large(arr):
    max = arr[0]

    for i in range(0,len(arr)):
        if arr[i] > max:
            max = arr[i]
    return max        
    


arr = [10,134,245,64,37256,477]
res = large(arr)
print(res)
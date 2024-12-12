def reverseArray(arr):

    left = 0
    right = len(arr) - 1

    while left <  right:

        arr[left], arr[right] = arr[right], arr[left]

        left+=1

        right-=1

arr=[12,31,5235,374,46,85,845,635]

reverseArray(arr)
for i in range(len(arr)):
        print(arr[i], end=" ")
        
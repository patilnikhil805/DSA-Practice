def rotateArray(arr, d):
    n = len(arr)

    for i in range(d):
        last = arr[n-1]

        for j in range(n-1, 0, -1):
            arr[j] = arr[j-1]
        arr[0] = last

arr = [1, 2, 3, 4, 5, 6]
d = 4

rotateArray(arr, d)

    # Print the rotated array
for i in range(len(arr)):
    print(arr[i], end=" ")
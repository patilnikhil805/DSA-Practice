# Two Pass Approach

def find (arr):
    largest = -1
    secondLargest = -1

    for i in range(0, len(arr)):
        if arr[i] > largest:
            largest = arr[i]
    
    for i in range(0,len(arr)):
        if arr[i] > secondLargest and arr[i] != largest:
            secondLargest = arr[i]
    return secondLargest

arr = [10,20,30,40]
res = find(arr)
print(res)
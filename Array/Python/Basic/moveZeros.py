# Python Program to move all zeros to end using two traversals

# Function which pushes all zeros to end
def pushZerosToEnd(arr):
    
    # Count of non-zero elements
    count = 0  

    # If the element is non-zero, replace the element at
    # index 'count' with this element and increment count
    for i in range(len(arr)):
        if arr[i] != 0:
            arr[count] = arr[i]
            count += 1

    # Now all non-zero elements have been shifted to
    # the front. Make all elements 0 from count to end.
    while count < len(arr):
        arr[count] = 0
        count += 1

if __name__ == "__main__":
    arr = [1, 2, 0, 4, 3, 0, 5, 0]
    pushZerosToEnd(arr)
    for num in arr:
        print(num, end=" ")
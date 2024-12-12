# Python program for find the largest 
# three elements in an array
def print3largest(arr):
    arr_size = len(arr)
    
    # There should be atleast three elements
    if arr_size < 3:
        print("Invalid Input")
        return
    
    third = first = second = float('-inf')
    
    for i in range(arr_size):
        # If current element is greater than first
        if arr[i] > first:
            third = second
            second = first
            first = arr[i]
        
        # If arr[i] is in between first and second then update second
        elif arr[i] > second and arr[i] != first:
            third = second
            second = arr[i]
        
        elif arr[i] > third and arr[i] != second and arr[i] != first:
            third = arr[i]

    print("Three largest elements are", first, second, third)

# Driver code
arr = [12, 13, 1, 10, 34, 11, 34]
print3largest(arr)

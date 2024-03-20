# Let's say you have an array of integers and you need to find the maximum sum of a subarray of a fixed size k.

def max_subarray_sum(arr, k):
    if k > len(arr):
        return "Invalid input"
    
    max_sum = float('-inf')  # Initialize max_sum to negative infinity
    window_sum = sum(arr[:k])  # Compute the sum of the first k elements
    max_sum = max(max_sum, window_sum)  # Update max_sum
    
    # Slide the window across the array
    for i in range(1, len(arr) - k+1 ):
        window_sum = window_sum - arr[i - 1] + arr[i + k - 1]  # Update window_sum
        max_sum = max(max_sum, window_sum)  # Update max_sum
    
    return max_sum

# Example usage
arr = [4, 2, 1, 7, 8, 1, 2, 8, 1, 8]
k = 3
print("Maximum sum of subarray of size", k, ":", max_subarray_sum(arr, k))


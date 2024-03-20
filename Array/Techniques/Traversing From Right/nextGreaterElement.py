# Let's consider the problem of finding the next greater element for each element in an array.

# Problem Statement:
# Given an array of integers, return an array where each element represents the next greater element for that element. If there is no next greater element, consider it as -1.

# Example:
# Input: [4, 6, 3, 2, 8, 1]
# Output: [6, 8, 8, 8, -1, -1]

# Explanation:
# For element 4, the next greater element is 6.
# For element 6, the next greater element is 8.
# For elements 3, 2, and 1, there are no greater elements to their right, so we put -1.

# Approach:
# Initialize an array to store the result, initially filled with -1.
# Iterate through the input array in reverse order.
# Initialize a variable max_right to keep track of the maximum element encountered from the right side so far. Initially, set max_right to -1.
# For each element:
# Compare the current element with max_right.
# If the current element is greater than max_right, update the result array at the current index with the value of the current element.
# Update max_right to be the maximum of the current element and max_right.
# Return the result array.


# Yes, it's possible to achieve the same result without using a stack, although it might require a slightly different approach. Instead of using a stack, you can directly manipulate the result array while traversing the input array from right to left. Here's how you can modify the approach to eliminate the stack:

# Approach:
# Initialize an array to store the result, initially filled with -1.
# Iterate through the input array in reverse order.
# Initialize a variable max_right to keep track of the maximum element encountered from the right side so far. Initially, set max_right to -1.
# For each element:
# Compare the current element with max_right.
# If the current element is greater than max_right, update the result array at the current index with the value of the current element.
# Update max_right to be the maximum of the current element and max_right.
# Return the result array.
# Code Implementation (in Python):



def next_greater_elements(nums):
    n = len(nums)
    result = [-1] * n
    max_right = -1
    
    for i in range(n - 1, -1, -1):
        if nums[i] >= max_right:
            max_right = nums[i]
        else:
            j = i + 1
            while j < n and nums[j] <= nums[i]:
                j += 1
            if j < n:
                result[i] = nums[j]
    
    return result

# Example usage:
nums = [4, 6, 3, 2, 8, 1]
print(next_greater_elements(nums))  # Output: [6, 8, 8, 8, -1, -1]


# Explanation:
# We start from the right end of the array [4, 6, 3, 2, 8, 1].
# We initialize max_right to -1.
# We iterate from the right end.
# At each step, we compare the current element with max_right.
# If the current element is greater than max_right, we update the result array at the current index with the value of the current element.
# We update max_right to be the maximum of the current element and max_right.
# We continue this process until we traverse the entire array.
# Finally, we return the result array.
# This approach also has a time complexity of O(n), where n is the size of the input array, as we traverse the array only once. However, it does not require the use of an explicit stack data structure.
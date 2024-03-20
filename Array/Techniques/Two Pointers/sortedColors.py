# Problem Statement:
# We're given an array nums containing objects colored red, white, or blue, represented by the integers 0, 1, and 2 respectively. We need to sort the objects in-place so that objects of the same color are adjacent.

# Approach:
# We'll utilize the Two Pointers technique again, with three pointers this time, to partition the array into three sections: red, white, and blue. The idea is to swap elements and move pointers accordingly to achieve the desired sorting.

# Step-by-Step Explanation:
# Initialize Pointers:

# left: Points to the current position where the next 0 should be placed.
# right: Points to the current position where the next 2 should be placed.
# curr: Starts from the beginning of the array and traverses it.
# Traversal and Swapping:

# We iterate through the array using the curr pointer:
# If nums[curr] is 0, we swap it with the element at nums[left] and increment both curr and left.
# If nums[curr] is 2, we swap it with the element at nums[right] and decrement right.
# If nums[curr] is 1, we simply increment curr.
# Termination:

# We continue this process until curr surpasses right, indicating that all elements have been sorted.
# Example with Values:
# Let's consider the example array:

# python
# Copy code
# nums = [2, 0, 2, 1, 1, 0]
# Initialize pointers:

# left = 0
# right = 5
# curr starts from nums[0].
# Traversal and Swapping:

# nums[curr] (2) is 2, so we swap it with nums[right] (0). Now, nums becomes [0, 0, 2, 1, 1, 2], and decrement right to 4.

# nums[curr] (0) is 0, so we swap it with nums[left] (2). Now, nums becomes [0, 0, 2, 1, 1, 2], and increment curr and left.

# nums[curr] (0) is 0, so we swap it with nums[left] (2). Now, nums becomes [0, 0, 2, 1, 1, 2], and increment curr and left.

# nums[curr] (1) is 1, so we increment curr.

# nums[curr] (1) is 1, so we increment curr.

# nums[curr] (2) is 2, so we swap it with nums[right] (1). Now, nums becomes [0, 0, 1, 1, 2, 2], and decrement right to 3.

# Termination:

# We stop when curr surpasses right.
# Finally, the sorted nums becomes [0, 0, 1, 1, 2, 2], achieving the desired sorting order.


nums = [2, 0, 2, 1, 1, 0]


def sortColors(nums):
    left = 0
    right = len(nums) - 1
    curr = 0
    
    while curr <= right:
        if nums[curr] == 0:
            nums[curr], nums[left] = nums[left], nums[curr]
            left += 1
            curr += 1
        elif nums[curr] == 2:
            nums[curr], nums[right] = nums[right], nums[curr]
            right -= 1
        else:
            curr += 1

sortColors(nums)
print(nums)  # Output: [0, 0, 1, 1, 2, 2]

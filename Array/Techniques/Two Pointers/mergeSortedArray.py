# Problem Statement:
# We are given two arrays of integers, nums1 and nums2, where nums1 has extra space at the end to accommodate elements from nums2. The task is to merge nums2 into nums1 in sorted order.

# Approach:
# We'll use the Two Pointers technique to solve this problem efficiently. The basic idea is to compare elements from both arrays and place the larger one at the end of nums1, working backwards.

# Step-by-Step Explanation:
# Initialize Pointers: We initialize three pointers:

# p1: Points to the last valid element in nums1.
# p2: Points to the last element in nums2.
# p: Points to the last position in nums1, where the merged elements will be placed.
# Comparison and Merging:

# We start comparing elements from the end of both arrays (p1 and p2).
# If the element at nums1[p1] is greater than the element at nums2[p2], we place it at position p in nums1, and decrement p1.
# Otherwise, we place the element at nums2[p2] at position p in nums1, and decrement p2.
# We continue this process until we have processed all elements in nums1 or nums2.
# Handling Remaining Elements:

# After the above loop, there might be remaining elements in nums2 that haven't been merged yet.
# We copy these remaining elements from nums2 to the beginning of nums1, starting from position p.
# Example with Values:
# Let's take the same example values as before:

# python
# Copy code
# nums1 = [1, 3, 5, 0, 0, 0]
# nums2 = [2, 4, 6]
# Here, m = 3 and n = 3.

# Initialize pointers:

# p1 = 2 (last valid index in nums1)
# p2 = 2 (last index in nums2)
# p = 5 (last index in merged array)
# Comparison and Merging:

# We start comparing elements from the end:

# nums1[p1] (5) > nums2[p2] (6), so we place 5 at nums1[p] and decrement p1.
# Now, p1 = 1, p = 4.
# nums1[p1] (3) > nums2[p2] (6), so we place 3 at nums1[p] and decrement p1.

# Now, p1 = 0, p = 3.
# nums1[p1] (1) < nums2[p2] (6), so we place 6 at nums1[p] and decrement p2.

# Now, p2 = 1, p = 2.
# Handling Remaining Elements:

# All elements from nums2 have been merged. No action required.
# Finally, the merged nums1 becomes [1, 2, 3, 4, 5, 6].






nums1 = [1, 3, 5, 0, 0, 0]
nums2 = [2, 4, 6]



def merge(nums1, m, nums2, n):
    p1 = m - 1
    p2 = n - 1
    p = m + n - 1
    
    while p1 >= 0 and p2 >= 0:
        if nums1[p1] > nums2[p2]:
            nums1[p] = nums1[p1]
            p1 -= 1
        else:
            nums1[p] = nums2[p2]
            p2 -= 1
        p -= 1
    
    while p2 >= 0:
        nums1[p] = nums2[p2]
        p2 -= 1
        p -= 1

merge(nums1, 3, nums2, 3)
print(nums1)


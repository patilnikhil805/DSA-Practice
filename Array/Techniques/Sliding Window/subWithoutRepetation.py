# 3. Longest Substring Without Repeating Characters
# Medium
# Topics
# Companies
# Given a string s, find the length of the longest 
# substring
#  without repeating characters.

 

# Example 1:

# Input: s = "abcabcbb"
# Output: 3
# Explanation: The answer is "abc", with the length of 3.
# Example 2:

# Input: s = "bbbbb"
# Output: 1
# Explanation: The answer is "b", with the length of 1.
# Example 3:

# Input: s = "pwwkew"
# Output: 3
# Explanation: The answer is "wke", with the length of 3.
# Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.
 

# Constraints:

# 0 <= s.length <= 5 * 104
# s consists of English letters, digits, symbols and spaces.

def length_of_longest_substring(s):
    if not s:
        return 0
    
    max_length = 0
    char_index = {}
    start = 0
    
    for end in range(len(s)):
        if s[end] in char_index:
            start = max(start, char_index[s[end]] + 1)
        
        char_index[s[end]] = end
        max_length = max(max_length, end - start + 1)
    
    return max_length

# Initialization:

# s = "abcabcbb"
# max_length = 0: This variable keeps track of the maximum length of the substring without repeating characters.
# char_index = {}: This dictionary will store the most recent index of each character encountered.
# start = 0: This variable marks the start of the current substring being examined.
# Iterating over the string:
# We'll iterate over the string "abcabcbb" character by character using a sliding window technique.

# 1st iteration (index 0):

# end = 0, s[end] = "a".
# Since "a" is encountered for the first time, char_index["a"] is updated to 0.
# No repeating characters, so max_length = max(0, 0 - 0 + 1) = 1.
# 2nd iteration (index 1):

# end = 1, s[end] = "b".
# "b" is encountered for the first time, so char_index["b"] is updated to 1.
# No repeating characters, so max_length = max(1, 1 - 0 + 1) = 2.
# 3rd iteration (index 2):

# end = 2, s[end] = "c".
# "c" is encountered for the first time, so char_index["c"] is updated to 2.
# No repeating characters, so max_length = max(2, 2 - 0 + 1) = 3.
# 4th iteration (index 3):

# end = 3, s[end] = "a".
# "a" is encountered again. char_index["a"] is 0, so we update start to max(0, 0 + 1) = 1.
# The substring now starts from index 1.
# No repeating characters, so max_length remains 3.
# 5th iteration (index 4):

# end = 4, s[end] = "b".
# "b" is encountered again. char_index["b"] is 1, so start remains 1.
# The substring now starts from index 1.
# No repeating characters, so max_length remains 3.
# 6th iteration (index 5):

# end = 5, s[end] = "c".
# "c" is encountered again. char_index["c"] is 2, so start remains 1.
# The substring now starts from index 1.
# No repeating characters, so max_length remains 3.
# 7th iteration (index 6):

# end = 6, s[end] = "b".
# "b" is encountered again. char_index["b"] is 4, so start is updated to max(1, 4 + 1) = 5.
# The substring now starts from index 5.
# No repeating characters, so max_length remains 3.
# 8th iteration (index 7):

# end = 7, s[end] = "b".
# "b" is encountered again. char_index["b"] is 7, so start is updated to max(5, 7 + 1) = 6.
# The substring now starts from index 6.
# No repeating characters, so max_length remains 3.
# Return:
# The final value of max_length is 3, which is the length of the longest substring without repeating characters. So, the function returns 3.

# This explains how the code works for the given input string "abcabcbb".

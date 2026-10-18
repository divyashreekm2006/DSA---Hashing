"""
Problem: Largest Consecutive Sequence
Description: Find the length of the longest consecutive numbers .

Example:
Input: arr = [100, 4, 200, 1, 3, 2]
Output: 4 (sequence: 1, 2, 3, 4)
"""

def largest_consecutive(arr):
    nums = set(arr)
    longest = 0

    for num in nums:
        if num - 1 not in nums:  # Check if it's the start of a sequence
            length = 1
            while num + length in nums:
                length += 1
            longest = max(longest, length)
    return longest

arr = [100, 4, 200, 1, 3, 2]
print(largest_consecutive(arr))
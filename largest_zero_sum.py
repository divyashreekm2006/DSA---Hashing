"""
Problem: Largest Subarray with Zero Sum

Description:
find the length of the longest contiguous subarray with a sum of zero.

Example:
Input: arr = [1, 2, -3, 3, 1, -4, 2]
Output: 5 (subarray: [2, -3, 3, 1, -4])
"""

def largest_zero_sum(arr):
    prefix_sum = 0
    first_index ={0: -1}
    longest = 0

    for i, num in enumerate(arr):
        prefix_sum += num
        if prefix_sum in first_index:
            lonest = max(lonest, i - first_index[prefix_sum])
        else:
            first_index[prefix_sum] = i
    return longest

arr = [1, 2, -3, 3, 1, -4, 2]
print(largest_zero_sum(arr))
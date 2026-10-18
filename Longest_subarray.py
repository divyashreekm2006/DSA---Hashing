"""
Problem: Find the length of the longest subarray whose sum equals k

Description:
Given an array of integers and an integer k, find the length of the longest contiguous subarray

example:
Input: arr = [1, -1, 5, -2, 3], k = 3
Output: 4 (subarray: [1, -1, 5, -2])
"""

def longest_subarray_with_sum_k(arr, k):
    prefix_sum = 0
    first_index = {0: -1}
    longest = 0

    for i, num in enumerate(arr):
        prefix_sum += num
        if prefix_sum - k in first_index:
            longest = max(longest, i - first_index[prefix_sum - k])
        if prefix_sum not in first_index:
            first_index[prefix_sum] = i

    return longest

arr = [1, -1, 5, -2, 3]
k = 3   
print(longest_subarray_with_sum_k(arr, k))
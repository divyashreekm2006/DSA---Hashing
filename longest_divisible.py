"""
Problems: Find the longest subarray with a sum divisible by k

Description:
Given an array of integers and a value k, find the length of the longest contiguous subarray whose sum is divisible by k.

Example:
Input: arr = [4, 5, 0, -1, 0, 1, -1], k = 5
Output: 5 (subarray: [5, 0, -1, 0, 1])
"""

def longest_divisible_subarray(arr, k):
    prefix_sum = 0
    first_index = {0: -1}
    longest = 0

    for i, num in enumerate(arr):
        prefix_sum += num
        remainder = prefix_sum % k

        if remainder in first_index:
            longest = max(longest, i - first_index[remainder])
        else:
            first_index[remainder] = i

    return longest

arr = [4, 5, 0, -1, 0, 1, -1]
k = 5
print(longest_divisible_subarray(arr, k))
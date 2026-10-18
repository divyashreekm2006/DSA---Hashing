"""
problems : Find the longest substring with equal number of 0s and 1s

Description : Given a binary array, find the length of the longest contiguous subarray with equal number of 0s and 1s.

Example:
Input: arr = [0, 1, 0, 1, 1,1, 0]
output : 4

"""

def longest_equal_subarray(arr):
    prefix_sum = 0
    first_index = {0: -1}
    longest = 0

    for i, num in enumerate(arr):
        if num == 0:
            prefix_sum -= 1
        else:
            prefix_sum += 1

        if prefix_sum in first_index:
            longest = max(longest, i - first_index[prefix_sum])
        else:
            first_index[prefix_sum] = i

    return longest

arr = [0, 1, 0, 1, 1, 1, 0]
print(longest_equal_subarray(arr))
"""
Problem: Count subarrays with sum k

Description:
Count the contiguous subarrays whose sum equals k.

Example:
Input: arr = [1, 2, 3], k = 3   
Output: 2 (subarrays: [1, 2], [3])
"""

def count_subarrays_with_sum_k(arr, k):
    frequency = {0: 1}
    prefix_sum = 0
    count = 0

    for num in arr:
        prefix_sum += num
        needed_sum = prefix_sum - k
        count += frequency.get(needed_sum, 0)
        frequency[prefix_sum] = frequency.get(prefix_sum, 0) + 1
    return count

arr = [1, 2, 3]
k = 3
print(count_subarrays_with_sum_k(arr, k))

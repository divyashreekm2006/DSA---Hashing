"""
Problem: Count Distinct elements in Every Window

Description:
Count the number of distinct elements in each sliding window of size k.

Example:
Input: arr = [1, 2, 1, 3, 2], k = 3
Output: [2, 3, 2] (distinct elements in each window)
"""

def count_distinct_in_windows(arr, k):
    result = []

    if k <= 0 or k > len(arr):
        return result
    for i in range(len(arr) - k + 1):
        window = arr[i:i + k]
        result.append(len(set(window)))
    return result

arr = [1, 2, 1, 3, 2]
k = 3   
print(count_distinct_in_windows(arr, k))

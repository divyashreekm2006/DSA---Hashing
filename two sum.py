"""
Problem: Two sum

Description: Find the indices of two elements whose sum is equal to a given target valu

Example:
Input: arr = [2, 7, 11, 15], target = 9
Output: [0, 1] 
"""

def two_sum(arr, target):
    seen = {}
    for i, num in enumerate(arr):
        complement = target - num
        if complement in seen:
            return [seen[complement], i]
        seen[num] = i
    return []

arr = [2, 7, 11, 15]
target = 9
print(two_sum(arr, target))
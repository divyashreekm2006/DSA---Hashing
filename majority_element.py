"""
Problem: Majority Element

Description: Find the element that appears more than n/2 times  return -1 if no such element exists in an array of size n.

Example:
Input: arr = [3,3,4,2, 3,3,3]
Output: 3
"""

def majority_element(arr):
    freq = {}
    for num in arr:
        freq[num] = freq.get(num, 0) + 1
        if freq[num] > len(arr) // 2:
            return num
    return -1

arr = [3, 3, 4, 2, 3, 3, 3]
print(majority_element(arr))
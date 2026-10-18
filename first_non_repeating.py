"""
Problem: Find the first non-repeating element in a list.

Description:
Given a list of integers, find the first element that appears exactly once.

Example:
Input: [1, 2, 3, 2, 4, 5, 1]
Output: 3
"""
def first_non_repeating(lst):
    frequency = {}
    for num in lst:
        frequency[num] = frequency.get(num, 0) + 1

    for num in lst:
        if frequency[num] == 1:
            return num
    return -1

s = [1, 2, 3, 2, 4, 5, 1]
print(first_non_repeating(s)) 
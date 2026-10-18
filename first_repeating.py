"""
Problem: Find the first repeating element in a list.

Description:
Given a list of integers, find the first element that appears more than once.

Example:
Input: [1, 2, 3, 2, 4, 5, 1]
Output: 2
"""
def first_repeating(lst):
    seen = set()
    for num in lst:
        if num in seen:
            return num
        seen.add(num)
    return -1
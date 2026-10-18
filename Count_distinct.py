"""
problem: Count the frequency of each element in a list.

Description : count the number of unique elements in an array

Example:
Input:[1,2,2,3,4,4,5]
Output: 5
"""

def count_distinct(arr):
    return len(set(arr))

arr = [1,2,2,3,4,4,5]
print(count_distinct(arr))
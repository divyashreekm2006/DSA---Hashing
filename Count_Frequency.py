"""
Problem: Count the frequency of each element in a list.

Description :
Count how many times each element appears in an array

Example:
Input: [1,2,2,3,1,2]
Output: {1: 2, 2: 3, 3: 1}
"""
def count_frequency(lst):
    frequency = {}
    for num in lst:
        if num in frequency:
            frequency[num] += 1
        else:   
            frequency[num] = 1
    return frequency
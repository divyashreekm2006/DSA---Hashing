"""
Problem: Find the intersection of two arrays.

Description:
Given two arrays, find the elements that are common to both arrays.

Example:
Input: arr1 = [1, 2, 3, 4], arr2 = [3, 4, 5, 6]
Output: [3, 4]
"""
def intersection(arr1, arr2):
    second = set(arr2)
    seen = set()
    result = []

    for num in arr1:
        if num in second and num not in seen:
            result.append(num)
            seen.add(num)

    return result

arr1 = [1, 2, 3, 4]
arr2 = [3, 4, 5, 6]
print(intersection(arr1, arr2))
    
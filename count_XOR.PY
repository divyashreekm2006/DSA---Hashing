"""
Problems: Count pairs with a given XOR

Description:
Count contiguous subarrays whose XOR equals k.

Example:
Input: arr = [4, 2, 2, 6, 4], k = 6
Output: 4 (subarrays: [4, 2], [2, 6], [6], [4, 2, 2, 6])
"""

def count_xor(arr, k):
    frequency = {0: 1}
    prefix_xor = 0
    count = 0

    for num in arr:
        xor_value^= num
        needed_xor = prefix_xor ^ k
        count += frequency.get(needed_xor, 0)

        frequency[prefix_xor] = frequency.get(prefix_xor, 0) + 1

    return count

arr = [4, 2, 2, 6, 4]
k = 6
print(count_xor(arr, k))
"""
problem : Minimum Window Substring

Description : Find the smallest substring of s containing all characters of t with the required frequency.

Example:
Input: s = "ADOBECODEBANC", t = "ABC"   
output : "BANC"
"""

from collections import Counter

def min_window(s, t):
    if not s or not t:
        return ""

    need = Counter(t)
    left = 0
    missing = len(t)
    start = 0
    min_length = float("inf")

    for right, ch in enumerate(s):
        if need[ch] > 0:
            missing -= 1

        need[ch] -= 1

        while missing == 0:
            length = right - left + 1

            if length < min_length:
                min_length = length
                start = left

            left_char = s[left]
            need[left_char] += 1

            if need[left_char] > 0:
                missing += 1

            left += 1

    if min_length == float("inf"):
        return ""
    return s[start:start + min_length]

s = "ADOBECODEBANC"
t = "ABC"
print(min_window(s,t))

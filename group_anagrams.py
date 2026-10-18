"""
Problems: Group words that contain the same characters 

Description :
Given an array of strings, group the words that contain the same characters together.

Example:
Input: ["eat", "tea", "tan", "ate", "nat", "bat"]
Output: [["eat", "tea", "ate"], ["tan", "nat"], ["bat"]]
"""

def group_anagrams(words):
    groups = {}
    for word in words:
        key = tuple(sorted(word))

        if key not in groups:
            groups[key] = []
        groups[key].append(word)
    return list(groups.values())

words = ["eat", "tea", "tan", "ate", "nat", "bat"]
print(group_anagrams(words))
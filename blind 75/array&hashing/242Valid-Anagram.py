# Given two strings s and t, return true if t is an anagram of s, and false otherwise.

# An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

 

# Example 1:

# Input: s = "anagram", t = "nagaram"
# Output: true

# Example 2:

# Input: s = "rat", t = "car"
# Output: false


#my sol:
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        for i in s:
            if s.count(i) != t.count(i):
                return False
        for i in t:
            if s.count(i) != t.count(i):
                return False
        return True 

#op sol: youtube sol
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        a,b = {},{}
        for i in s:
            a[i] = s.count(i)
        for i in t:
            b[i] = t.count(i)
        return a==b



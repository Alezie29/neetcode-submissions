class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hashmap = {}

        if len (s) != len (t): # Different lengths means it can't be an anagram
            return False

        count_s = {}
        count_t = {}

        for ch in s:
            if ch in count_s:
                count_s[ch] += 1
            else:
                count_s[ch] = 1

        for ch in t:
            if ch in count_t:
                count_t[ch] += 1
            else:
                count_t[ch] = 1
        
        return count_s == count_t

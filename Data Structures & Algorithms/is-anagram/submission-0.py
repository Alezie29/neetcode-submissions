class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        countS, countT = {}, {} # Hashmap for letter and how many instances letter:instances
        
        for i in range(len(s)):
            countS[s[i]] = 1 + countS.get(s[i], 0) # in case there is no starting key, sets default value
            countT[t[i]] = 1 + countT.get(t[i], 0)
        for c in countS:
            if countS[c] != countT.get(c, 0):
                return False
        
        return True 


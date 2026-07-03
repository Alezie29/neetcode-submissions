class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # if lengths aren't the same then its not an anagram
        if len(s) != len(t):
            return False

        # create hashmaps storing s and t
        countS, countT = {},{}

        # go through each letter of s and t and add to hashmaps
        for i in range(len(s)):
            countS[s[i]] = 1 + countS.get(s[i], 0)
            countT[t[i]] = 1 + countT.get(t[i], 0)

        # use .get(#, 0) to prevent key error

        # check if the count of each character is the same in both hashmaps
        for character in countS:
            if countS[character] != countT.get(character, 0):
                return False
        
        return True
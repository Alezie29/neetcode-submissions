class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # if lengths arent same, not anagram
        if len(s) != len(t):
            return False

        # Create hashmaps
        countS, countT = {},{}

        # go through each character of S adding to hashmap with get(x, 0)
        for i in range(len(s)):
            countS[s[i]] = 1 + countS.get(s[i], 0)
            countT[t[i]] = 1 + countT.get(t[i], 0)

            # get(s, default = 0) is needed for first case of hashmap

       # checking if key is same for each hashmap 
        for key in countS:
            if countS[key] != countT.get(key, 0):
                return False

        return True

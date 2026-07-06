class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # Use an array of size O(26) to count the frequency of each character, then use this as the key in the hashmap.
        hashMap = {}

        for s in strs:
            alphabetArray = [0] * 26 # I want to make an array that allows up to 26 characters from a-z
            
            for char in s:
                alphabetArray[ord(char) - ord('a')] += 1

            key = tuple(alphabetArray) # Must be converted to tuple (immutable) so it can be the key for hashmap

            if key in hashMap:
                hashMap[key].append(s) # Add to current group (s)
            else:   
                hashMap[key] = [s] # Create a new group

        return list(hashMap.values()) # Return all anagrams as a list 


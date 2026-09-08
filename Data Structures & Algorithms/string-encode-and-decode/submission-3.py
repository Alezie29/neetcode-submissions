class Solution:

    # Prefixing with length (not just splitting on '#') avoids ambiguity if '#' appears inside a string itself

    def encode(self, strs: List[str]) -> str:
        res = "" # Encoded to a string
        for s in strs: # Loop through strs
            res += str(len(s)) + "#" + s # Make it the length of the string and a delimiter (e.g. 3#abc)
        return res
        
    def decode(self, s: str) -> List[str]:
        res, i = [], 0 # Returning a list in the end 
        
        while i < len(s):
            j = i # Need another index pointer
            while s[j] != "#": # Advance j until it lands on the '#', marking the end of the length digits
                j += 1
            length = int(s[i:j])
            res.append(s[j + 1 : j + 1 + length]) # Slice to get only the string, after delimter until next length int of next word
            i = j + 1 + length # Set this to next word or end 
        return res
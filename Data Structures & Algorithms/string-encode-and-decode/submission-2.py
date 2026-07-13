class Solution:
    def encode(self, strs: List[str]) -> str:
        # Setting an empty result that will be a string, then go through each string from the list
        # and create a new string ready for reading in the decode section. 
        # The length of the string, the separator, then the string itself.
        result = ""
        for s in strs:
            result += f"{len(s)}#{s}"  # e.g. "5#Hello5#World"
        return result

    def decode(self, s: str) -> List[str]:
        # Creating a list of strings back again, we set an initial pointer to the start
        # of the string, using a second pointer to go forward until we see the separator
        # a lenght variable stops the case where # is included in the strs
        #

        result = []
        i = 0

        while i < len(s):
            j = i
            while s[j] != "#":   # walk forward until we hit #
                j += 1
            
            length = int(s[i:j])          # everything before # is the length
            word = s[j+1 : j+1+length]    # read exactly 'length' chars after #
            result.append(word)
            i = j + 1 + length            # jump to start of next encoded string

        return result
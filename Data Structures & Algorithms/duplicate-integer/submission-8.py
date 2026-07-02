class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # Create a hash set
        seen = set() 

        # Go through nums and if it already exists in seen its a dupe
        for x in nums: 
            if x in seen:
                return True
                # if x is not in seen, add it to seen
            seen.add(x)
            # Gone through all of seen, there is no dupe
        return False
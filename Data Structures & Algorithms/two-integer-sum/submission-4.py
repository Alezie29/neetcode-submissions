class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash_table = {}

        for i, n in enumerate(nums): # Access nums with enumerate to also get index 
            complement = target - n # Easier readability
            if complement in hash_table: # Check first to stop two of the same letter being returned
                return [hash_table[complement], i] # Return with smaller value first 
            else:
                hash_table[n] = i # If not in hash_table, add the number to hashtable
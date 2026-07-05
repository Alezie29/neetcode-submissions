class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """" Create a hashmap where the key is the number and the 
        value is the index (easier to look up this way around).
        For example nums = [1, 3, 4, 5] target = [7]
        key: 1, value: 0 and so on. 
        before adding the value to the hashmap, first do the target minus 
        the number, this is the complement. If the complement exists in the 
        hashMap we return the complement and the current number as indices,
        if the complement does not exist, we add the current number to the
        hashMap. """
        
        hashMap = {} # Stores {number : index}

        for i, num in enumerate(nums): # Enumerate instead of num = nums[i]
            complement = target - num # Create a complement variable
        
            # if complement is in hashmap return it
            if complement in hashMap:
                return [hashMap[complement], i]
            hashMap[num] = i
            # else add that number to the hashMap
        


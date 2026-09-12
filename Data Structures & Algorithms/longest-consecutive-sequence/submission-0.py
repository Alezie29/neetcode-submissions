class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0

        nums = sorted(set(nums)) # Hash set removes duplicates

        longest = 1
        current = 1

        for i in range(1, len(nums)):
            if nums[i] == nums[i-1] + 1: # If the current number is the previous number + 1:
                current += 1 
                longest = max(longest, current) # Always have longest be the biggest number so far
            else:
                current = 1 # Break
        
        return longest
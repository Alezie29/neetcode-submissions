class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        prefix = [1] * n
        suffix = [1] * n
        result = [1] * n

        # build prefix (product of everything to the left)
        for i in range(1, n):
            prefix[i] = prefix[i-1] * nums[i-1] #-1 to go left 
            # prefix[2]= prefix[1] * nums[1] = 1 * 1 for example, the prefix array will update iteratively

        # build suffix (product of everything to the right)
        for i in range(n-2, -1, -1): # (start, stop, step)
            suffix[i] = suffix[i+1] * nums[i+1]

        # multiply them together
        for i in range(n):
            result[i] = prefix[i] * suffix[i]

        return result
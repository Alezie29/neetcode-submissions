class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # Pre initialize prefix and postfix arrays with 0s
        prefix = [0] * len(nums)
        postfix = [0] * len(nums)  

        # Populate start of prefix and end of postfix with 1
        prefix[0] = 1
        postfix[len(postfix)-1] = 1 

        res = []

        prod1 = 1
        prod2 = 1

        for i in range(1, len(nums)): # Start at 1 because 0 is already done (prefix[0] = 1) and because [0-1] = -1
            prod1 *= nums[i-1] # [i-1] says 'except self'
            # if it was i = 2, nums[2] = 4, but we want everything left of 4
            prefix[i] = prod1

        for i in range(len(prefix) -2, -1, -1): # postfix[last element] already = 1, -2 goes to second to last postfix = ([0,0,here,1])
            prod2 *= nums[i+1] # + 1 says after nums[i], i = 2, nums[3] and to the right
            postfix[i] = prod2

        for i in range(len(nums)): # Multiply prefix array with postfix array to get result array
            res.append(prefix[i] * postfix[i])
        return res
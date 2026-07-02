class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {} # Hashmap
        freq = [[] for i in range(len(nums) + 1)] # Empty array for the same amount of elements in input array + 1 [0 - 6]

        for n in nums: # Counting every value in nums
            count[n] = 1 + count.get(n, 0) # Default value of 0
        for n, c in count.items(): # Go through each value we counted (need to get key and value not just key)
            freq[c].append(n) # At index count we append the value
            # This value occurs c number of times

        res = [] # Creating new result array for output
        for i in range(len(freq) -1, 0, -1): # Go down in descending order from last value till 0
            for n in freq[i]: # Grab all numbers that appeared i times (can be multiple)
                res.append(n) # Append n to res
                if len(res) == k: # When res is the same amount of k we return
                    return res

        # O(n) Time
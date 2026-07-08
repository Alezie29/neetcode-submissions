class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Hashmap to store the count
        count = {}
        freq = [[] for i in range(len(nums) + 1)] # Building buckets for sorting

        for n in nums:
            count[n] = 1 + count.get(n, 0) # Go through each value in nums and count how many times it occurs
        for n, c in count.items(): # Go through each value we counted (key value pair) this value n occurs c number of times
            freq[c].append(n)

        res = [] 
        for i in range(len(freq) - 1, 0, -1): # Starting from the bottom, until 0, -1 as decrementer
            for n in freq[i]:
                res.append(n)
                if len(res) == k: # The number of values in the array matches K (e.g. 2)
                    return res
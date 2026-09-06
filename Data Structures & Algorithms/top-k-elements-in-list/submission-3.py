class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {} # Create a hashmap
        freq = [[] for i in range(len(nums) + 1)] # Create a list within an array, this will be where the values go +1 because 0 to length of array nums

        for n in nums: 
            count[n] = 1 + count.get(n, 0) # (n, 0) is default value for .get()
        for n, c in count.items(): #.items gets the key:value pair
            freq[c].append(n) # Append the value (list of values) to the current index (count) BUCKET SORTING

        res = [] # List for returning the result
        for i in range(len(freq) -1, 0, -1): # Starting from the last digit, go until 0, in descending order
            for n in freq[i]:
                res.append(n) # Adds numbers from list (found in values of dict) into a new results list
                if len(res) == k:
                    return res
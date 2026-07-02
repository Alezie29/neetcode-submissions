class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        group = set()

        for n in nums:
            if n in group:
                return True
            group.add(n)
        return False
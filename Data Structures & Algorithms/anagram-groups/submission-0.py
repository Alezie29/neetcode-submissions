from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_dict = defaultdict(list) # Mapping char count to anagrams list

        for s in strs:
            count = [0] * 26 
        
            for c in s:
                count[ord(c) - ord('a')] += 1

            anagram_dict[tuple(count)].append(s)

        return list(anagram_dict.values())
    
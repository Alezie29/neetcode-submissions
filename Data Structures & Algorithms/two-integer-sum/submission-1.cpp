class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        // make a hash table <number, index>
        unordered_map<int, int>seen;

        // key = int, value = index
        // nums = [0,1,2,3] key:0, value:0

        // add each int from nums to new hash 
        // find the 'complement' value (target - nums[i])
        // if the complement exists in the hasmap return the indices with i
        for (int i = 0; i < nums.size(); i++) {
            int complement = target - nums[i];
            if (seen.count(complement)) {
                return {seen[complement], i};
            } // else add the number with its indices
            seen[nums[i]] = i;
        }
        return {};
    }
};

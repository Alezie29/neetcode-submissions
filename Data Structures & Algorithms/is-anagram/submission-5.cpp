class Solution {
public:
    bool isAnagram(string s, string t) {
        if (s.length() != t.length()) return false;

        unordered_map<char, int> countS, countT;

        for (int i = 0; i < s.length(); i++) {
            countS[s[i]]++;
            countT[t[i]]++;
        }

        for (auto& [key, value] : countS) {
            if (countS[key] != countT[key]) return false;
        }

        return true;
    }   
};

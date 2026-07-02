class Solution {
    /**
     * @param {string} s
     * @param {string} t
     * @return {boolean}
     */
    isAnagram(s, t) {
        // edge case
    if (s.length !== t.length) return false;

    // creating a hashmap
    const map = {};

    // loop through s and add each letter to the map with a count starting from 1.
    for (let i = 0; i < s.length; i++) {
       let letter = s[i];
        
        if (!map[letter]) {
        map[letter] = 1;
        
        } else {
        map[letter]++;
        }
    }

    // loop through t and decrement the count until 0 is hit, returning true. 
   for (let i = 0; i < t.length; i++) {
    let letter = t[i];

        // edge cases
        if (map[letter] === undefined || map[letter] < 1) {
        return false;
    } map[letter]--; 
   }

   // if all edge cases pass 
    return true;
}
}
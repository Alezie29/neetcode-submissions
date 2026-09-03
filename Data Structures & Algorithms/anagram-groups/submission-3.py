class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
       # Make a hash table
       # Go through each string
       # Make an array of 26 0's representing the alphabet
       # Go through each character
       # We then increase the count of each letter to represent a string, anagrams will have the same array 
       # ord(ch) - ord(a) this will get the index from 0 to 26 that the letter represents 
       # Update the index in the array by 1
       # Turn the list into a tuple that will be used as a key in the hash table (lists can't be used)
       # The value will then be the list of strings (anagrams)
       # If the key (array sequence) has already been seen in the hashmap, append the string to it as a value 
       # If not, create a new list for the new key
       # Return only the values from the hash_table as a list
        
        hash_table = {}

        for s in strs: 
            count = [0] * 26 # Create an array of 0's represesnting alphabet
        
            for ch in s:
                index = ord(ch) - ord("a") # Find the index
                count[index] += 1 # Increase that letter's count by 1
            
            key = tuple(count) # Turning key into a tuple (lists can't be keys in a dict)
        
            if key in hash_table: # If the array sequence already exists
                hash_table[key].append(s) # Add that string to respective key as a value
            else:
                hash_table[key] = [s] # If it doesn't exist, make new key with string as value (list)
        
        return list(hash_table.values()) # Only the values from the hash_table
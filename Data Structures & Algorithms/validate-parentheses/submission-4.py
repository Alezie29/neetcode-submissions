class Solution:
    def isValid(self, s: str) -> bool:
       # Wanting to check that when each bracket appears, whatevery type, the closing bracket is expected after
       # However, you want the most recent open bracket to be 'at the top' so that their respective closing bracket is expected to appear first. 
       # This is where a stack could come in due to its first in last out order, ( added to the bottom postion 1, then { added to 2 and [ added to 3. The first expected closing bracket would be ] ('[' is at the top of the stack)
        stack = [] 
       
        for c in s:
            valid_p = ['{','}','(',')','[',']']
            opening_p = ['{', '(', '[']
            closing_p = ['}', ')', ']']
            pairs = {'}' : '{', ')' : '(', ']' : '['}
            
            if c not in valid_p:
                return False # Quick check that the character is actually a valid parentheses, if not return False
            
            if c in valid_p:
                if c in opening_p:
                    stack.append(c) # Add the valid opening parentheses to the stack
                
                if c in closing_p:
                    # Check if there's anything in the stack, if nothing then return False 
                    if len(stack) == 0:
                        return False
                        
                    top = stack.pop() # Store the top of the stack in a variable
                    if top != pairs[c]: # If the closing p doesn't match the opening p from dict, return False
                        return False
                # Check if it matches the opening_p at the top of the stack
        return len(stack) == 0
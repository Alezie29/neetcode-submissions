class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        valid_opening = ["(", "{", "["]
        valid_closing = [")", "}", "]"]
        valid_pair = {")" : "(", "}" : "{", "]" : "["}
        
        for c in s:   # loop over the STRING, not the stack
            if c in valid_opening:
                stack.append(c)
                
            elif c in valid_closing:
                # what do you do here? (hint: two things to check)
                # Check if the stack is empty, if so return False (e.g. ] is false)
                # Check if the respective opening parentheses is at the top of the stack
                if len(stack) == 0:
                    return False
                top = stack.pop() # Remove and grab the top item of the stack
                if top != valid_pair[c]:
                    return False

        if len(stack) != 0:
            return False # If there's any leftovers in the stack
        return True
        
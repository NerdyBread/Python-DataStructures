# Leetcode problem #20 using a stack


# In this problem I treat an array as a stack but the same idea applies

# I recommend you try to solve this problem before looking at my solution

# Github describes the problem like this:
""" 
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:
    Open brackets must be closed by the same type of brackets.
    Open brackets must be closed in the correct order.
"""

# Solution

def isValid(self, s: str) -> bool:
        stack = []  # Create an empty "stack"
        brackets = {'(': ')', '[': ']', '{': '}'}  # Hash table storing open brackets and closed brackets in key-value form
        
        for char in s:  # Loop through each character
            if char in brackets.keys():  
                # If char is an open bracket add it to the stack
                stack.append(char)
            else:
                # If it's a closed bracket do all this
                if stack:
                    # If stack isn't empty remove the top item and store it in "last"
                    last = stack.pop()
                else:
                    return False
                    # If the stack is empty and the program reaches this point the brackets are out of order
                if char != brackets[last]:
                    # If the current closed bracket isn't the last open bracket's equivalent: 
                    return False
                  
        # If we make it through the whole process without returning False perform a final check on the stack
        return not len(stack)
        # not len(stack) -> if len(stack) is 0 that equates to False, 'not' keyword flips that to True, if len(stack) isn't 0 the oppposite happens

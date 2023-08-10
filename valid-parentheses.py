class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        mapping = {')': '(', '}': '{', ']': '['}

        for char in s:
            if char in mapping.values():
                stack = stack + [char]
            elif char in mapping.keys():
                if stack and stack[-1] == mapping[char]:
                    stack = stack[:-1]
                else:
                    return False
            else:
                return False
    
        return len(stack) == 0

# Another way by using pop & append
def isValidParentheses(s):
    stack = []
    mapping = {')': '(', '}': '{', ']': '['}  # Mapping for closing and opening brackets

    for char in s:
        if char in mapping.values():  # If it's an opening bracket, push it onto the stack
            stack.append(char)
        elif char in mapping.keys():   # If it's a closing bracket
            if stack and stack[-1] == mapping[char]:  # Check if the stack is not empty and matches the opening bracket
                stack.pop()
            else:
                return False
        else:
            return False  # If the character is not a bracket, return False
    
    return not stack  # Return True if the stack is empty, False otherwise

# Test cases
print(isValidParentheses("()"))  # True
print(isValidParentheses("()[]{}"))  # True
print(isValidParentheses("(]"))  # False
print(isValidParentheses("([)]"))  # False
print(isValidParentheses("{[]}"))  # True

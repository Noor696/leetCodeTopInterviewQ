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

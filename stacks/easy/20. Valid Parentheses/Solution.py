from collections import deque

class Solution(object):
    def isValid1(self, s):
        stack = []

        closed = {  ')' : '(',
                    '}' : '{',
                    ']' : '['
                }

        for i in s:
            if i in closed:
                if stack[-1] == closed[i] and stack:
                    stack.pop()
                else: 
                    return False
            else: 
                stack.append(i)
                

        return True if not stack else False
    
    def isValid(self, s):
        if len(s) & 1 == 1:
            return False
        
        stack = deque()
        
        for char in s:
            if char == '(':
                stack.append('(')
            elif char == '[':
                stack.append('[')
            elif char == '{':
                stack.append('{')
            elif char == ')':
                if not stack or stack[-1] != '(':
                    return False
                stack.pop()
            elif char == ']':
                if not stack or stack[-1] != '[':
                    return False
                stack.pop()
            elif char == '}':
                if not stack or stack[-1] != '{':
                    return False
                stack.pop()
        
        return len(stack) == 0


print(Solution().isValid("()[]{}"))
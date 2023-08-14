class Solution(object):

    def evalRPN(self, tokens):
        stack = []

        for i in tokens:
            if i == '+':
                right = stack.pop()
                left = stack.pop()
                stack.append(left + right)
            elif i == '-':
                right = stack.pop()
                left = stack.pop()
                stack.append(left - right)
            elif i == '*':
                right = stack.pop()
                left = stack.pop()
                stack.append(left * right)
            elif i == '/':
                right = stack.pop()
                left = stack.pop()
                stack.append(int(left / right))
            else:
                stack.append(int(i))             

        return stack[0]


#,"3","*"
print(Solution().evalRPN(["10","6","9","3","+","-11","*","/","*","17","+","5","+"]))
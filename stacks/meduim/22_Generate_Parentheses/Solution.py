class Solution(object):
    def generateParenthesis(self, n):

        results = []
        entry = []

        def generate(open, closed):
            if open == closed == n:
                results.append("".join(entry))
                return
            
            if open < n:
                entry.append("(")
                generate(open+1, closed)
                entry.pop()

            if closed < open:
                entry.append(")")
                generate(open, closed+1)
                entry.pop()

        generate(0, 0)

        return results
    

print(Solution().generateParenthesis(4))
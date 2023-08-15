class Solution(object):
    def carFleet(self, target, position, speed):

        pairs = [[p, s] for p, s in zip(position, speed)]
        stack = []

        for p, s in sorted(pairs)[::-1]:
            distance = (target - p)/s
            stack.append(distance)
            if len(stack) >= 2 and stack[-2] < stack[-1]:
                stack.pop()
        return len(stack)

print(Solution().carFleet(12, [10,8,0,5,3], [2,4,1,1,3]))

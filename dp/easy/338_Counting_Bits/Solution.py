import math

class Solution(object):
    def countBits(self, n):
        binary = [0]
        msb = 1
        for i in range(1, n + 1):
            mbv = (2 ** msb)
            if mbv == i:
                msb+=1
                binary.append(1)
                continue
            length = len(binary)
            binary.append(1 + binary[length - mbv])
        return binary
    

sol = Solution()
print(sol.countBits(5))
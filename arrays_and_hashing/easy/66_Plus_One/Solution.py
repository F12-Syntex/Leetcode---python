class Solution(object):
    def plusOne(self, digits):
        for i in range(len(digits) - 1, -1, -1):
            if digits[i] == 9:
                digits[i] = 0
                continue
            else:
                digits[i]+=1
                return digits

        digits[0] = 1
        digits.append(0)
        return digits

        
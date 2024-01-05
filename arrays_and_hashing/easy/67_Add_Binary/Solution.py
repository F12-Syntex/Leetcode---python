class Solution(object):
    def addBinary(self, a, b):

        if len(a) < len(b):
            a, b = b, a

        res = ""
        carry = 0

        for i in range(len(a)):

            bIndex = len(b) - i - 1
            aIndex = len(a) - i - 1

            ca = a[aIndex]
            cb = '0'

            if bIndex >= 0:
                cb = b[bIndex]

            binSum = int(ca) + int(cb) + carry

            if binSum == 3:
                res = '1' + res
                carry = 1
            elif binSum == 2:
                res = '0' + res
                carry = 1
            elif binSum == 1:
                res = '1' + res
                carry = 0
            else:
                res = '0' + res
                carry = 0

        if carry > 0:
            res = '1' + res

        return res
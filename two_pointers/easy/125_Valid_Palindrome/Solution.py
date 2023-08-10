class Solution(object):
    def isPalindrome(self, s):
        text = s.lower()
        length = len(text) 

        leftPointer = 0
        rightPointer = length - 1


        while leftPointer < rightPointer:

            while (leftPointer < rightPointer) and not (text[leftPointer].isdigit() or text[leftPointer].isalpha()):
                leftPointer += 1
                

            while (leftPointer < rightPointer) and not (text[rightPointer].isdigit() or text[rightPointer].isalpha()):
                rightPointer -= 1


            print(text[leftPointer], "-", text[rightPointer])
            if text[leftPointer] != text[rightPointer]:
                return False
            leftPointer+=1
            rightPointer-=1

        return True


print(Solution().isPalindrome(".,"))
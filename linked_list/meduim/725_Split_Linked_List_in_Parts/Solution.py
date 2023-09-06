# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __str__(self) -> str:
        res = str(self.val)
        if self.next:
            res += "->" + str(self.next)
        return res


class Solution(object):
    def splitListToParts(self, head, k):

        length = 0
        cur = head
        
        dummy = head
        node = dummy

        while cur:
            cur = cur.next
            length+=1

        res = []
        for i in range(k):
            output = []
            baseNumber = length // k
            excess = length % k
            
            requried = baseNumber
            if excess > 0:
                requried += 1
                length -= 1

            if requried == 0:
                res.append(None)
                continue

            #get kth node
            cHead = node
            tail = node
            for j in range(1, requried):
                tail = tail.next

            # print("group: ", cHead, tail)
            node = tail.next
            tail.next = None
            res.append(cHead)
            
        return res



# linkedlist1 = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
linkedlist2 = ListNode(1, ListNode(2, ListNode(3)))
print(Solution().splitListToParts(linkedlist2, 5))
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
    def removeNthFromEnd(self, head, n):
        
        dummy = ListNode(0, head)

        l = dummy
        r = head

        for i in range(n):
            r = r.next

        while r:
            l = l.next
            r = r.next

        l.next = l.next.next
        head = dummy.next
        print(head)


linkedlist1 = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
linkedlist2 = ListNode(1)
linkedlist3 = ListNode(1, 2)
Solution().removeNthFromEnd(linkedlist1, 2)
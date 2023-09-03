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
    def reorderList(self, head):
        s, f = head, head.next

        #partition
        while f and f.next:
            s = s.next
            f = f.next.next

        p1 = head
        p2 = s.next

        s.next = prev = None
        
        #reverse
        while p2:
            nxt = p2.next
            p2.next = prev
            prev = p2
            p2 = nxt
        p2 = prev

        #merge
        while p2:
            tmp1, tmp2 = p1.next, p2.next
            p1.next = p2
            p2.next = tmp1
            p1 = tmp1
            p2 = tmp2 

        print(head)



linkedlist = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
print(Solution().reorderList(linkedlist))
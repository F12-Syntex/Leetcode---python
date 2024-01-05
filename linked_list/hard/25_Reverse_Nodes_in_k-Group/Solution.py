class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __str__(self) -> str:
        res = str(self.val)
        if self.next:
            res += "->" + (str(self.next))
        return res

class Solution(object):
    def reverseKGroup(self, head, k):

        dummy = ListNode(0, head)
        groupPrev = dummy

        while True:
            kth = self.getKthElement(groupPrev, k)

            #the gruop does not exist, so lets just break out
            if not kth:
                break

            groupNext = kth.next

            #reverse the group where the head is the next groups head  
            # 1 -> 2 -> 3 -> 4   where k is 2
            # ^---------v
            # 2 -> 1    3 -> 4
            prev, curr = kth.next, groupPrev.next
            while curr != groupNext:
                nxt = curr.next
                curr.next = prev
                prev = curr
                curr = nxt

            tmp = groupPrev.next
            groupPrev.next = kth
            groupPrev = tmp
            

        return dummy.next
    
    def getKthElement(self, cur, k):
        while cur and k > 0:
            cur = cur.next
            k-=1
        return cur

    
        
linkedlist1 = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
print(Solution().reverseKGroup(linkedlist1, 2))
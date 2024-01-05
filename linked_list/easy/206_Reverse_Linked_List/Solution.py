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
    def reverseList(self, head):
        
        curr, prev = head, None

        while curr:
            #save the next list to explore
            nxt = curr.next

            #set the current val's next to the prev node
            curr.next = prev

            #set the new prev to explore, which is the curr nodes minus the curr value
            prev = curr

            #set the new curr to explore which is just the original next value
            curr = nxt

        return prev
    
linkedlist = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
print(Solution().reverseList(linkedlist))
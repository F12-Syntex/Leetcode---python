# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    
    def __str__(self) -> str:
        return str(self.val)

    
class Solution(object):
    def print(self, head):
        print(head)

        if head.next != None:
            self.print(head.next) 

    def reverseList(self, head):
        prev = None
        current = head

        while current is not None:
            next = current.next
            current.next = prev
            prev = current
            current = next
        
        return prev
        


node = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5, ListNode(6, ListNode(7, ListNode(8))))))))
solution = Solution() 
solution.print(solution.reverseList(node)) 

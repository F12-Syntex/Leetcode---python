# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def deleteDuplicates(self, head):
        cur = head
        prev = None
        while cur:
            nxt = cur.next
            if prev and cur.val == prev.val:
                self.removeNode(cur, prev)
            else:
                prev = cur

            cur = nxt
        return head

    def removeNode(self, node, prev):
        nxt = node.next

        #tail, we already know that the tail is not null
        if not nxt:
            prev.next = None
            return

        prev.next = nxt
        node.next = None
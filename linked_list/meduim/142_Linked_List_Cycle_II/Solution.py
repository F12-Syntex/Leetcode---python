class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __str__(self) -> str:
        res = str(self.val)
        if self.next:
            res += "->" + (str(self.next.val) if self.next else "None")
        return res


class Solution(object):
    def hasCycle(self, head):
        mapping = set()
        while head:
            if head.next in mapping:
                return head.next
            mapping.add(head)
            head = head.next
        return None
    


node4 = ListNode(-4)
node3 = ListNode(0)
node2 = ListNode(2)
node1 = ListNode(3)

node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node2

print(Solution().hasCycle(node1))
        
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
    def hasCycle2(self, head):

        mapping = {}
        index = 0

        while head:
            if head.next in mapping:
                return mapping[head.next]
            
            mapping[head] = index
            
            head = head.next
            index += 1 


        return -1
    
    def hasCycle(self, head):
        l, r = head, head
        while r.next and r.next.next:
            l = l.next
            r = r.next.next
            if l == r:
                return True
        return False

    


node4 = ListNode(-4)
node3 = ListNode(0)
node2 = ListNode(2)
node1 = ListNode(3)

node1.next = node2
node2.next = node3
node3.next = node4
# node4.next = node2

print(Solution().hasCycle(node1))
        
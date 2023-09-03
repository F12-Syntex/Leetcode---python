class ListNode(object):
    def __init__(self, x, nxt=None, random=None):
        self.val = int(x)
        self.next = nxt
        self.random = random

    def __str__(self) -> str:
        res = str(self.val) + "(" + str(self.random) + ")"
        if self.next:
            res += "->" + str(self.next)
        return res


class Solution(object):
    def copyRandomList(self, head):

        #map all the nodes
        mapping = {
            None : None
        }

        curr = head
        while curr:
            mapping[curr] = ListNode(curr.val)
            curr = curr.next

        #create the deep copy
        curr = head
        while curr:
            #original node is curr
            #clones node is mapping[cur]
            copy = mapping[curr]

            copy.next = mapping[curr.next]
            copy.random = mapping[curr.random]

            curr = curr.next

        return mapping[head]
    
node5 = ListNode(1, None, None)

node4 = ListNode(10, node5, node5)
node3 = ListNode(11, node4, node5)
node2 = ListNode(13, node3, node4)
node1 = ListNode(7, node2, node3)

print(Solution().copyRandomList(node1))
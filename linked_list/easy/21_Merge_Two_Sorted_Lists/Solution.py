class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __str__(self) -> str:
        res = str(self.val)
        if self.next:
            res += "->" + str(self.next)
        return res
    
class Solution():
    def mergeTwoLists(self, list1, list2):
        root = ListNode()
        tail = root

        while list1 and list2:
            if list1.val < list2.val:
                tail.next = list1
                list1 = list1.next
            else:
                tail.next = list2
                list2 = list2.next
            tail = tail.next

        if list1:
            tail.next = list1
        elif list2:
            tail.next = list2

        return root.next

linkedlist1 = ListNode(1, ListNode(2, ListNode(4)))
linkedlist2 = ListNode(1, ListNode(3, ListNode(4)))
print(Solution().mergeTwoLists(linkedlist1, linkedlist2))
        
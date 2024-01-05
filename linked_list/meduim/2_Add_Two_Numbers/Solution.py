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
    def addTwoNumbersSol1(self, l1, l2):

        p1 = ""
        p2 = ""

        prev = None
        while l1:
            nxt = l1.next
            l1.next = prev
            prev = l1
            l1 = nxt
        l1 = prev

        prev = None
        while l2:
            nxt = l2.next
            l2.next = prev
            prev = l2
            l2 = nxt
        l2 = prev

        while l1:
            p1 += str(l1.val)
            l1 = l1.next

        while l2:
            p2 += str(l2.val)
            l2 = l2.next

        ans = str(int(p1) + int(p2))

        res = ListNode(0)
        root = res

        for r in range(len(ans) - 1, -1, -1):
            c = int(ans[r])
            res.next = ListNode(c)
            res = res.next

        return root.next
    
    def addTwoNumbers(self, l1, l2):

        stack1, stack2 = [], []

        while l1:
            stack1.append(l1.val)
            l1 = l1.next

        while l2:
            stack2.append(l2.val)
            l2 = l2.next

        num1, num2 = "", ""

        while stack1:
            num1 += str(stack1.pop())

        while stack2:
            num2 += str(stack2.pop())

        res = str(int(num1) + int(num2))

        root = ListNode()
        ans = root

        for r in range(len(res) - 1, -1, -1):
            ans.next = ListNode(res[r])
            ans = ans.next

        return root.next
    
linkedlist1 = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
linkedlist2 = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
print(Solution().addTwoNumbers(linkedlist1, linkedlist2))
        
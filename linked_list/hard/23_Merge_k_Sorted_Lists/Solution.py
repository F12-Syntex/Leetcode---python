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
    def mergeKLists(self, lists):

        #check if the lists are valid
        if not lists and len(lists) == 0:
            return None

        #we will do a merge sort sorting two ll at a time
        while len(lists) > 1:
            currentlySorted = []
            for i in range(0, len(lists), 2):
                list1 = lists[i]
                list2 = lists[i + 1] if (i + 1) < len(lists) else None
                currentlySorted.append(self.mergeTwoLists(list1, list2))
            lists = currentlySorted
        return lists[0]
    
    def mergeTwoLists(self, list1, list2):
        dummy = ListNode(0)
        root = dummy
        while list1 and list2:
            if list1.val < list2.val:
                root.next = list1
                list1 = list1.next
            else:
                root.next = list2
                list2 = list2.next
            root = root.next
        if list1:
            root.next = list1
        elif list2:
            root.next = list2
        return dummy.next
        
linkedlist1 = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
linkedlist2 = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
linkedlist3 = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))

print(Solution().mergeKLists([linkedlist1, linkedlist2, linkedlist3]))
# print(Solution().mergeTwoLists(linkedlist1, linkedlist2))
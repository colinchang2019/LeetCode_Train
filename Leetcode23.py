# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        if len(lists)<1:
            return lists
        left,right = 0,len(lists)-1
        while left<right:
            mid = (left+right)//2
            for i in range(mid+1):
                if i!=right-i:
                    lists[i] = self.merge2Lists(lists[i],lists[right-i])
            right = mid
        return lists[0]

    def merge2Lists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        head = ListNode(0)
        first = head
        while l1!=None and l2!=None:
            if l1.val <= l2.val:
                head.next = l1
                l1 = l1.next
            else:
                head.next = l2
                l2 = l2.next
            head = head.next
        if l1 != None:
            head.next = l1
        elif l2 != None:
            head.next = l2
        return first.next

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        n1,n2 = 0,0
        h1,h2 = l1,l2
        while h1:
            h1 = h1.next
            n1 += 1
        while h2:
            h2 = h2.next
            n2 += 1
        if n1<n2:
            n1,n2 = n2,n1
            l1,l2 = l2,l1
        li = [0]*n1
        for i in range(n1):
            li[i] += l1.val
            l1 = l1.next
            if i+n2>=n1:
                li[i] += l2.val
                l2 = l2.next
        x = 0
        for i in range(n1):
            j = n1 - i - 1
            x,li[j] = divmod((x + li[j]),10)
        head = ListNode(x)
        res = head
        for i in li:
            x = ListNode(i)
            head.next = x
            head = head.next
        return res if res.val else res.next

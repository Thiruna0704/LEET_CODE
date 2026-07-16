# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        

        n1 = ""
        while l1:
            n1 = str(l1.val) + n1
            l1 = l1.next

        n2 = ""
        while l2:
            n2 = str(l2.val) + n2
            l2 = l2.next

        total = int(n1) + int(n2)

        dummy = ListNode(0)
        curr = dummy

        for digit in str(total)[::-1]:
            curr.next = ListNode(int(digit))
            curr = curr.next

        return dummy.next
        
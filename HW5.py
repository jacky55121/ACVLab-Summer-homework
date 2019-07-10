# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        n1=l1
        a=0
        n2=l2
        b=0
        head=ListNode(0)
        temp=head
        while n1 or n2:
            if n1 or n2:
                if n1 and n2:
                    if n1.val<=n2.val:
                        a=n1.val
                        temp.next=ListNode(a)
                        temp=temp.next
                        n1=n1.next
                    else:
                        b=n2.val
                        temp.next=ListNode(b)
                        temp=temp.next
                        n2=n2.next
                elif n1:
                    a=n1.val
                    temp.next=ListNode(a)
                    temp=temp.next
                    n1=n1.next
                elif n2:
                    b=n2.val
                    temp.next=ListNode(b)
                    temp=temp.next
                    n2=n2.next
        return head.next
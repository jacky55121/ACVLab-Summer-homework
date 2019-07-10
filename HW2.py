# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        n1=l1
        a=0
        a1=0
        n2=l2
        b=0
        b1=0
        while n1:
            a=a+(n1.val*(10**a1))
            a1+=1
            n1=n1.next
        while n2:
            b=b+(n2.val*(10**b1))
            b1+=1
            n2=n2.next
        c=a+b
        z=[]
        if c==0:z.append(0)
        while (c != 0):
            z.append(c%10)
            c=c//10
        head=ListNode(0)
        temp=head
        for tans in z:
            temp.next=ListNode(tans)
            temp=temp.next
        return head.next
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeNthFromEnd(self, head, n: int):
        if head==None or head.next == None and n==1: return None
        if head.next.next==None :
            if n==1:
                head.next=None
                return head
            else:
                return head.next
        fp=sp = head
        for i in range(1,n):
            sp=sp.next
        while sp :
            if sp.next == None:
                fp.next=fp.next.next
            fp=fp.next
            sp=sp.next
        return head

l5=ListNode(5,None)
l4=ListNode(4,l5)
l3=ListNode(3,)
l2=ListNode(2,l3)
l1=ListNode(1,l2)
obj=Solution()
print(obj.removeNthFromEnd(l1,3))
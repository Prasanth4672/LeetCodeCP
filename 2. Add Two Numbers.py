# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def addTwoNumbers(self, l1, l2):
        head=temp=ListNode()
        carry=0
        while l1 or l2 or carry:
            l1_val= l1.val if l1 else 0
            l2_val= l2.val if l2 else 0
            total = l1_val+l2_val+carry
            temp.next = ListNode(total%10)
            carry=total//10

            l1=l1.next if l1 else None
            l2=l2.next if l2 else None

            temp=temp.next

        return (head.next).val
    

obj = Solution()
#List1
l1=ListNode(2)
l1.next=ListNode(4)
l1.next.next=ListNode(3)

#List2

l2=ListNode(5)
l2.next=ListNode(6)
l2.next.next=ListNode(4)

print(obj.addTwoNumbers(l1,l2))
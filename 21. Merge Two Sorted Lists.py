# Definition for singly-linked list.
class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next
class Solution:
    def mergeTwoLists(self, list1, list2):
        head=temp=ListNode()
        while list1 and list2:
            if list1.val < list2.val:
                temp.next=list1
                list1=list1.next
            else:
                temp.next=list2
                list2=list2.next
            temp=temp.next
        temp.next=list1 or list2
        return (head.next).val


obj = Solution()
#List1
l1=ListNode(1)
l1.next=ListNode(2)
l1.next.next=ListNode(4)

#List2

l2=ListNode(1)
l2.next=ListNode(3)
l2.next.next=ListNode(4)


print(obj.mergeTwoLists(l1,l2))

        





        


      

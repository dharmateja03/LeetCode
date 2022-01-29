# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        a= ListNode(0)
        p=a
        if l1==None:
            return l2
        elif l2==None:
            return l1
        if l1.val<=l2.val:
            head=tail=l1
            l1=l1.next
        else:
            head=tail=l2
            l2=l2.next
        while(l1 and l2):
            if l1.val<=l2.val:
                tail.next=l1
                tail=l1
                l1=l1.next
                
                
            else:
                tail.next=l2
                tail=l2
                l2=l2.next
                
        if l1==None:
            tail.next=l2
        else:
            tail.next=l1
        return head
        
                    
                
        
        
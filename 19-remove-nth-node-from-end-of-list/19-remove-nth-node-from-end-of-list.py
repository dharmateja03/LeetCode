# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        curr=head
        if head==None or head.next==None:
            return None
        dumy=ListNode(0)
        dumy.next=head
        while(n):
            curr=curr.next
            n-=1
        curr1=head
        if curr==None:
            dumy.next=head.next
            return dumy.next
        while(curr.next):
            curr1=curr1.next
            curr=curr.next
        curr1.next=curr1.next.next
        return head
        
        
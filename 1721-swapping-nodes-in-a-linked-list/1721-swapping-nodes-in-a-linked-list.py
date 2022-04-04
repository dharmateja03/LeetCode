# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: ListNode, k: int) -> ListNode:
        slow,fast=head,head
        for i in range(k-1):
            fast=fast.next
        temp1=fast
        while(fast.next!=None):
            slow=slow.next
            fast=fast.next
        temp2=slow
        temp1.val,temp2.val=temp2.val,temp1.val
        return head
        
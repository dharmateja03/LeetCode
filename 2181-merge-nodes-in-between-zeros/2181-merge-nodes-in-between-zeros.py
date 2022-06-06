# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        a= ListNode(0)
        b= ListNode(0)
        a.next=b

        b=a.next
        while(head):
            ans=0
            while(head and head.val):
                ans+=head.val
                head=head.next
            h=a
            b.next=ListNode(ans)
            b=b.next
            head=head.next
        return a.next.next.next
                
        
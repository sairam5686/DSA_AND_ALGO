# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        low , high = head , head
        previous = low

        if(head.next == None):
            return None
        if(head.next.next == None):
            head.next = None
            return head
        while(high.next is not None and high.next.next is not None ):
            previous = low
            low = low.next
            high = high.next.next

        if(high.next != None):
            low = low.next
            previous = previous.next

        previous.next = low.next
        return head
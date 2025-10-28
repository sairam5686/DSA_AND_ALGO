# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        if(head is None or head.next is None):
            return head
        New_Header = head.next
        even_ptr = New_Header
        odd_ptr = head
        prev_odd_ptr = None
        while(  (odd_ptr is not None) and (odd_ptr.next is not None)  ):
            prev_odd_ptr = odd_ptr
            odd_ptr.next = odd_ptr.next.next
            odd_ptr = odd_ptr.next

            if(((even_ptr.next is not None) and (even_ptr.next.next is not None))):
                even_ptr.next = even_ptr.next.next
                even_ptr = even_ptr.next
                # print(even_ptr.data)

        if(prev_odd_ptr.next != None):
            prev_odd_ptr = prev_odd_ptr.next
        even_ptr.next = None
        prev_odd_ptr.next = New_Header

        return  head
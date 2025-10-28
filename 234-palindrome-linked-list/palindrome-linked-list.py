# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        low , high = head , head

        if(head.next is None):
            return True
        while(high is not None and high.next is not None and high.next.next is not None):
            low  = low.next
            high = high.next.next


        New_header = low.next
        low.next = None
        current = New_header
        previous = None
        while(current is not None):
            future = current.next
            current.next = previous
            previous  = current
            current = future


        ptr_1 , ptr_2 = head  , previous
        flag = False
        while(ptr_2 is not None):
            if(ptr_1.val == ptr_2.val):
                flag = True
                ptr_1 = ptr_1.next
                ptr_2 =ptr_2.next
            else:
                return False
        return flag

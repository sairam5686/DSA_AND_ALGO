# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def modifiedList(self, nums: List[int], head: Optional[ListNode]) -> Optional[ListNode]:
        DNode = ListNode(-1)
        DNode.next  = head
        prev  = DNode
        current = DNode.next
        nums = set(nums)
        while(current):

            if(current.val  in nums):
                prev.next = current.next
                current  = current.next
            else:
                prev = prev.next
                current = current.next

        return DNode.next
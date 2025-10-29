# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
def merge_two_ll(list1 , list2):
    dummy_node = ListNode(-1)
    temp = dummy_node
    ptr_1 , ptr_2 = list1 , list2
    while(ptr_1 is not None and ptr_2 is not None):
        if(ptr_1.val <= ptr_2.val):
            temp.next = ptr_1
            temp = temp.next
            ptr_1 = ptr_1.next
            temp.next = None
        else:
            temp.next = ptr_2
            temp = temp.next
            ptr_2 = ptr_2.next
            temp.next = None
    while(ptr_1 is not None):
        temp.next = ptr_1
        temp = temp.next
        ptr_1 = ptr_1.next
        temp.next = None
    while(ptr_2 is not None):
        temp.next = ptr_2
        temp = temp.next
        ptr_2 = ptr_2.next
        temp.next = None

    return dummy_node.next


def LL_sort(head):
    if(head is None or head.next is None):
        return head
    slow , fast = head , head
    while(fast.next is not None and fast.next.next is not None):
        slow = slow.next
        fast = fast.next.next



    right_head= slow.next
    slow.next = None
    left_head = head
    left = LL_sort(left_head)
    right = LL_sort(right_head)
    return merge_two_ll(left , right)

class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
       return LL_sort(head)
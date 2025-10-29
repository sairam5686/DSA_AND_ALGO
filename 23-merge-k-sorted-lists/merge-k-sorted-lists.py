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
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if(len(lists  ) ==  0):
            return None
        head = lists[0]
        for i in range(1 , len(lists)):
            head = merge_two_ll(head , lists[i])
        return head
        
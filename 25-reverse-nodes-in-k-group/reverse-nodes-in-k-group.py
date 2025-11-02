# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

def reverser(head):
    previous , current = None,head
    while(current):
        future = current.next
        current.next = previous
        previous = current
        current = future
    return previous


def K_locator(head , k):
    while( head and  k != 1 ):
        head = head.next
        k -=1
    return head

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        current = head
        prev_Node = None
        while(current):
            kth = K_locator(current , k)
            if(kth is None):
                if(prev_Node):
                    prev_Node.next = current
                break
            new_header = kth.next
            kth.next = None
            reverse_head = reverser(current)
            # print(current.data)
            if(head == current ):
                head = kth
                # print(kth.data)
            else:
                prev_Node.next = kth
            prev_Node = current
            current = new_header
        return head
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        turtle , rabbit = head , head
        while(1):
            if(rabbit is None or rabbit.next is None):
               return False
            else:
                turtle = turtle.next
                rabbit = rabbit.next.next
                if(turtle == rabbit):
                    return True
            
        return False
            

        

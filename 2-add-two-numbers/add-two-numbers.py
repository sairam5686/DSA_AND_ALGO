# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self,headA , headB):
        ptr1 = headA
        ptr2 = headB
        Dummy_node = ListNode(-1)
        ptr_temp = Dummy_node
        remainder =  0
        while(ptr1 and ptr2):
            Total_value  = (ptr1.val + ptr2.val + remainder)
            remainder =((Total_value) //10 )
            # print(Total_value , remainder)
            temp = ListNode((Total_value)%10)
            ptr_temp.next = temp
            ptr_temp = ptr_temp.next
            ptr1 = ptr1.next
            ptr2 = ptr2.next

        while(ptr1 != None):
            Total_value = (ptr1.val  + remainder)
            remainder =((Total_value)  //10 )

            temp = ListNode(Total_value %10)
            ptr_temp.next = temp
            ptr_temp = ptr_temp.next
            ptr1 = ptr1.next

        while (ptr2 != None):
            Total_value = (ptr2.val + remainder)
            remainder = ((Total_value) // 10)
            temp = ListNode((Total_value)%10)
            ptr_temp.next = temp
            ptr_temp = ptr_temp.next
            ptr2 = ptr2.next
        if(remainder != 0):
            temp = ListNode(remainder)
            ptr_temp.next = temp


        return Dummy_node.next
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        temp_list1 = []
        temp_list2 = []
        
        curr1 = l1
        while curr1:
            temp_list1.append(curr1.val)
            curr1 = curr1.next

        curr2 = l2
        while curr2:
            temp_list2.append(curr2.val)
            curr2 = curr2.next

        temp_list1.reverse()
        temp_list2.reverse()

        l1_str = "".join(map(str, temp_list1))
        l2_str = "".join(map(str, temp_list2))

        final_str = int(l1_str) + int(l2_str)
        final_list = list(str(final_str))
        final_listt = []

        for digit in final_list:
            final_listt.append(int(digit))
            
        final_listt.reverse()
        dummy = ListNode()
        curr = dummy
        for val in final_listt:
            curr.next = ListNode(val)
            curr = curr.next
        return dummy.next

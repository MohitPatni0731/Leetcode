# https://leetcode.com/problems/merge-two-sorted-lists/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        temp_list_1 = []
        temp_list_2 = []

        curr1 = list1

        while curr1:
            temp_list_1.append(curr1.val)
            curr1 = curr1.next
        
        curr2 = list2
        while curr2:
            temp_list_2.append(curr2.val)
            curr2 = curr2.next
        
        result = temp_list_1 + temp_list_2
        result.sort()

        #return result
        
        dummy = ListNode()
        curr = dummy
        for val in result:
            curr.next = ListNode(val)
            curr = curr.next
        return dummy.next

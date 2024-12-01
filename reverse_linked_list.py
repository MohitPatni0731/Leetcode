# https://leetcode.com/problems/reverse-linked-list/description/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = head
        temp_list = []
        while curr:
            temp_list.append(curr.val)
            curr = curr.next
        temp_list.reverse()

        dummy = ListNode()
        curr = dummy
        for val in temp_list:
            curr.next = ListNode(val)
            curr = curr.next
        return dummy.next

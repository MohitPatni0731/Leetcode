# https://leetcode.com/problems/remove-nth-node-from-end-of-list/description/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        temp_head = []
        curr = head
        while curr:
            temp_head.append(curr.val)
            curr = curr.next
        
        temp_head.pop(-n)

        dummy = ListNode()
        curr = dummy
        for val in temp_head:
            curr.next = ListNode(val)
            curr = curr.next
        return dummy.next

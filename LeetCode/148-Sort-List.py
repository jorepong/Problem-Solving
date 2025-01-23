# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def merge(self, node1, node2):
        if node1 and node2:
            if node1.val > node2.val:
                node1, node2 = node2, node1
            node1.next = self.merge(node1.next, node2)
        return node1 or node2


    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not (head and head.next):
            return head

        prev, slow, fast = None, head, head
        while fast and fast.next:
            prev, slow, fast = slow, slow.next, fast.next.next
        prev.next = None

        left = self.sortList(head)
        right = self.sortList(slow)

        return self.merge(left, right)

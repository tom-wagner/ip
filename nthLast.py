# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

# two pass
# class Solution:
#     def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
#         list_size = self.size(head)
#         idx_to_remove = list_size - n
#         return self.remove_and_return(head, idx_to_remove)
#
#     def remove_and_return(self, head: ListNode, idx_to_remove: int):
#         if idx_to_remove == 0:
#             return head.next
#
#         idx = 1
#         prev, curr = head, head.next
#         while True:
#             if idx < idx_to_remove:
#                 idx += 1
#                 curr = curr.next
#                 prev = prev.next
#             elif idx == idx_to_remove:
#                 prev.next = curr.next
#                 break
#
#         return head
#
#     def size(self, head: ListNode):
#         length = 0
#         curr = head
#         while curr:
#             length += 1
#             curr = curr.next
#
#         return length


# one pass
class Solution:
    def __init__(self):
        self.nodes = {}

    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        idx = 0
        curr = head
        while curr:
            self.nodes[idx] = curr
            idx += 1
            curr = curr.next
        node_to_remove = idx - n

        if node_to_remove == 0:
            return head.next

        self.nodes[idx - n - 1].next = self.nodes[idx - n].next
        return head




    # def remove_and_return(self, head: ListNode, idx_to_remove: int):
    #     if idx_to_remove == 0:
    #         return head.next
    #
    #     idx = 1
    #     prev, curr = head, head.next
    #     while True:
    #         if idx < idx_to_remove:
    #             idx += 1
    #             curr = curr.next
    #             prev = prev.next
    #         elif idx == idx_to_remove:
    #             prev.next = curr.next
    #             break
    #
    #     return head

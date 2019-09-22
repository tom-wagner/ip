# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def get_smaller_and_return_lists(l1: ListNode, l2: ListNode):
    if l1 and l2:
        if l1.val < l2.val:
            return l1.val, l1.next, l2
        else:
            return l2.val, l1, l2.next
    if l1:
        return l1.val, l1.next, l2
    if l2:
        return l2.val, l1, l2.next
    return None, None, None


class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        head = tail = None
        while l1 or l2:
            value_to_add, l1, l2 = get_smaller_and_return_lists(l1, l2)
            if not head:
                head = tail = ListNode(value_to_add)
            else:
                tail.next = ListNode(value_to_add)
                tail = tail.next
        return head

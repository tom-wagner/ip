from typing import List, Tuple, Dict

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def get_min_head_detail(list_maps: Dict[int, ListNode]) -> Tuple[int, int]:
    min_list_num = min_val = None
    for k, v in list_maps.items():
        if min_val is None or v.val < min_val:
            min_list_num = k
            min_val = v.val
    return min_list_num, min_val


class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        head = tail = None
        lists_map = {idx: l for idx, l in enumerate(lists) if l}
        while len(lists_map) > 0:
            min_list_num, min_val = get_min_head_detail(lists_map)
            if not head:
                head = tail = lists_map[min_list_num]
            else:
                tail.next = lists_map[min_list_num]
                tail = tail.next

            if lists_map[min_list_num].next:
                lists_map[min_list_num] = lists_map[min_list_num].next
            else:
                del lists_map[min_list_num]

        return head

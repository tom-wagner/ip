import binarytree
import random


def get_parent_idx(idx):
    return (idx - 1) // 2


def get_child_indices(idx: int):
    """return left and right indices for a given node"""
    return 2 * idx + 1, 2 * idx + 2


def get_larger_idx(l_val: int, l_idx: int, r_val: int, r_idx: int):
    if l_val and r_val:
        return l_idx if l_val >= r_val else r_idx
    elif l_val and not r_val:
        return l_idx
    elif r_val and not l_val:
        return r_idx
    else:
        return None


class MaxHeap:
    def __init__(self):
        self.heap = binarytree.tree(height=3, is_perfect=True).values

    def print(self):
        print(binarytree.build(self.heap))

    def sort(self):
        n = len(self.heap) - 1
        for idx in range(n // 2, -1, -1):
            self.heapify_down(idx)

    def swap(self, i, j):
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]

    def v(self, idx):
        return self.heap[idx] if len(self.heap) > idx else None

    def add_value(self, val):
        self.heap.append(val)
        idx = len(self.heap) - 1
        parent_idx = get_parent_idx(idx)
        did_swap = True
        while did_swap and parent_idx >= 0:
            did_swap, _, top_idx = self.heapify(parent_idx)
            parent_idx = top_idx and get_parent_idx(top_idx)

    def heapify_down(self, idx):
        did_swap, bottom_idx, _ = self.heapify(idx)
        if did_swap and bottom_idx:
            self.heapify(bottom_idx)

    def heapify(self, idx):
        """return boolean stating whether swap occurred, and if so return bottom idx and top idx"""
        l_idx, r_idx = get_child_indices(idx)

        l_val, r_val = self.v(l_idx), self.v(r_idx)
        larger_child_idx = get_larger_idx(l_val=l_val, l_idx=l_idx, r_val=r_val, r_idx=r_idx)

        if larger_child_idx and self.heap[larger_child_idx] > self.heap[idx]:
            self.swap(larger_child_idx, idx)
            return True, larger_child_idx, idx

        return False, None, None


mh = MaxHeap()
mh.sort()
mh.print()

for _ in range(150):
    x = random.randint(1, 1000)
    mh.add_value(x)

mh.print()

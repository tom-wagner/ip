
# START TIME: 4:01pm


def get_parent_idx(idx):
    return (idx - 1) // 2


def get_larger_child_idx(heap, idx):
    left_child_idx, right_child_idx = (idx * 2) + 1, (idx * 2) + 2
    left_child = heap[left_child_idx] if left_child_idx < len(heap) else None
    right_child = heap[right_child_idx] if right_child_idx < len(heap) else None

    if left_child and right_child:
        return left_child_idx if left_child >= right_child else right_child_idx
    if left_child:
        return left_child_idx
    return None


class Heap:
    def __init__(self, arr):
        self.heap = arr
        self.init()

    def init(self):
        heap_size = len(self.heap)
        for idx in range(heap_size // 2, -1, -1):
            self.heapify(idx, should_heapify_down=True)

    def heapify(self, idx: int, should_heapify_down: bool = False, should_heapify_up: bool = False):
        larger_child_idx = get_larger_child_idx(self.heap, idx)
        if larger_child_idx and self.heap[idx] < self.heap[larger_child_idx]:
            self.heap[idx], self.heap[larger_child_idx] = self.heap[larger_child_idx], self.heap[idx]
            if should_heapify_up:
                parent_idx = get_parent_idx(idx)
                if parent_idx >= 0:
                    self.heapify(parent_idx, should_heapify_up=True)
            if should_heapify_down:
                self.heapify(larger_child_idx, should_heapify_down=True)

    def contains(self, x):
        return x in set(self.heap)

    def add(self, x):
        self.heap.append(x)
        parent_idx_of_elem_just_added = get_parent_idx(len(self.heap) - 1)
        self.heapify(parent_idx_of_elem_just_added, should_heapify_up=True)

    def pop(self):
        last_idx = len(self.heap) - 1
        self.heap[0], self.heap[last_idx] = self.heap[last_idx], self.heap[0]
        tmp = self.heap.pop()
        self.heapify(0, should_heapify_down=True)
        return tmp


h = Heap([5, 6, 1, 2, 12, 17, 9, 4, 8, 23, 16, 7, 19, 21])

h.add(26)
h.add(15)
h.add(-16)

print('h contains 8', h.contains(8))
print('h does not contain 923', not h.contains(923))
print('h should pop 26', h.pop() == 26)
print('h should pop 23', h.pop() == 23)
print('h should pop 21', h.pop() == 21)

# END TIME: 4:12pm

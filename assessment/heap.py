
# START TIME: 12:37pm

get_parent_idx = lambda idx: (idx // 2) - 1
get_child_indices = lambda idx: (2 * idx + 1, 2 * idx + 2)


def get_larger_child_idx(idx, heap):
    left_child_idx, right_child_idx = get_child_indices(idx)
    if left_child_idx <= len(heap) - 1 and right_child_idx <= len(heap) - 1:
        return left_child_idx if heap[left_child_idx] >= heap[right_child_idx] else right_child_idx
    if left_child_idx <= len(heap) - 1:
        return left_child_idx
    if right_child_idx <= len(heap) - 1:
        return right_child_idx
    return None


class Heap:
    def __init__(self, arr):
        self.heap = arr
        self.init()

    def init(self):
        for idx in range(len(self.heap) // 2, -1, -1):
            self.heapify(idx, should_heapify_down=True)

    def heapify(self, idx, should_heapify_down=False, should_heapify_up=False):
        larger_child_idx = get_larger_child_idx(idx, self.heap)

        if larger_child_idx and self.heap[larger_child_idx] > self.heap[idx]:
            self.heap[idx], self.heap[larger_child_idx] = self.heap[larger_child_idx], self.heap[idx]
            if should_heapify_down:
                self.heapify(larger_child_idx, should_heapify_down=True)
            if should_heapify_up:
                parent_idx = get_parent_idx(idx)
                if parent_idx >= 0:
                    self.heapify(parent_idx, should_heapify_up=True)

    def contains(self, x):
        return x in set(self.heap)

    def add(self, x):
        self.heap.append(x)
        new_last_idx = len(self.heap) - 1
        parent_idx = get_parent_idx(new_last_idx)
        self.heapify(parent_idx, should_heapify_up=True)

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

# END TIME: 12:56pm

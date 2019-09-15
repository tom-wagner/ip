
# START TIME: 10:03pm


def get_parent_idx(i):
    return (i - 1) // 2


def get_child_indices(i):
    return i * 2 + 1, i * 2 + 2


def get_larger_child_idx(heap, l_idx, r_idx):
    last_idx = len(heap) - 1
    if l_idx <= last_idx and r_idx <= last_idx:
        return l_idx if heap[l_idx] >= heap[r_idx] else r_idx
    if l_idx <= last_idx:
        return l_idx
    if r_idx <= last_idx:
        return r_idx


class Heap:
    def __init__(self, arr):
        self.heap = arr
        self.init(arr)

    def init(self, arr):
        for i in range(len(arr) // 2, -1, -1):
            self.heapify(i, should_heapify_down=True)

    def heapify(self, idx, should_heapify_down=False, should_heapify_up=False):
        left_child_idx, right_child_idx = get_child_indices(idx)
        larger_child_idx = get_larger_child_idx(self.heap, left_child_idx, right_child_idx)

        if larger_child_idx and self.heap[idx] <= self.heap[larger_child_idx]:
            self.heap[idx], self.heap[larger_child_idx] = self.heap[larger_child_idx], self.heap[idx]
            if should_heapify_down:
                self.heapify(larger_child_idx, should_heapify_down=True)
            if should_heapify_up:
                parent_idx = get_parent_idx(idx)
                if parent_idx >= 0:
                    self.heapify(parent_idx, should_heapify_up=True)

    def add(self, x):
        self.heap.append(x)
        last_idx = len(self.heap) - 1
        parent_idx = get_parent_idx(last_idx)
        self.heapify(parent_idx, should_heapify_up=True)

    def contains(self, x):
        return x in set(self.heap)

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

# END TIME: 10:26pm

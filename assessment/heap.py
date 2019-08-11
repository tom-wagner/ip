# START TIME: 6:28pm


def get_children(idx, heap):
    left_child_idx, right_child_idx = 2*idx + 1, 2*idx + 2

    try:
        left = heap[left_child_idx]
    except:
        left = None
    try:
        right = heap[right_child_idx]
    except:
        right = None

    return left, left_child_idx, right, right_child_idx


def get_larger_child(left, left_idx, right, right_idx):
    if left and right:
        return (left, left_idx) if left > right else (right, right_idx)
    elif left:
        return left, left_idx
    elif right:
        return right, right_idx
    else:
        return None, None


def get_parent_idx(idx):
    return (idx - 1) // 2


class Heap:
    def __init__(self, arr):
        self.heap = arr
        for idx in range(len(arr) // 2, -1, -1):
            self.heapify(idx, should_heapify_down=True)
        print(self.heap)

    def heapify(self, idx, should_heapify_down=False, should_heapify_up=False):
        left, left_idx, right, right_idx = get_children(idx, self.heap)

        larger_child, larger_child_idx = get_larger_child(left, left_idx, right, right_idx)

        if larger_child and larger_child > self.heap[idx]:
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
        last_idx = len(self.heap) - 1
        self.heapify(get_parent_idx(last_idx), should_heapify_up=True)

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

# END TIME: 6:47pm

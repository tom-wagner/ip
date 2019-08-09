
# START TIME: 8:16am


class Heap:
    def __init__(self, arr):
        self.heap = arr
        self.init()

    def check(self):
        # TO CHECK HEAP
        for idx, val in enumerate(self.heap):
            l, r = 2*idx + 1, 2*idx + 2
            try:
                print(val, self.heap[l], self.heap[r])
            except:
                pass

    def init(self):
        for i in range(len(self.heap) // 2 - 1, -1, -1):
            self.heapify(i, should_heapify_down=True)

    def get_children_for_idx(self, idx):
        left_idx, right_idx = 2 * idx + 1, 2 * idx + 2

        try:
            left = self.heap[left_idx]
        except:
            left = None
        try:
            right = self.heap[right_idx]
        except:
            right = None

        return left, left_idx, right, right_idx

    def heapify(self, idx, should_heapify_down=False, should_heapify_up=False):
        val = self.heap[idx]
        left, left_idx, right, right_idx = self.get_children_for_idx(idx)

        if left and right:
            larger_child, larger_child_idx = (left, left_idx) if left >= right else (right, right_idx)
        elif right:
            larger_child, larger_child_idx = right, right_idx
        elif left:
            larger_child, larger_child_idx = left, left_idx
        else:
            return

        if val < larger_child:
            self.heap[idx], self.heap[larger_child_idx] = self.heap[larger_child_idx], self.heap[idx]
            if should_heapify_down:
                self.heapify(larger_child_idx, should_heapify_down=True)
            if should_heapify_up:
                parent_idx = (idx - 1) // 2
                if parent_idx >= 0:
                    self.heapify(parent_idx, should_heapify_up=True)

    def contains(self, x):
        return x in set(self.heap)

    def add(self, x):
        self.heap.append(x)
        last_idx = len(self.heap) - 1
        parent_idx = (last_idx - 1) // 2
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

# h.check()

print('h contains 8', h.contains(8))
print('h does not contain 923', not h.contains(923))
print('h should pop 26', h.pop() == 26)
print('h should pop 23', h.pop() == 23)
print('h should pop 21', h.pop() == 21)

# END TIME: 8:45am


# START TIME: 6:18pm


def get_child_indices(idx):
    return (2*idx + 1), (2*idx + 2)


def get_parent_idx(idx):
    return (idx - 1) // 2


class Heap:
    def __init__(self, arr):
        self.arr = arr
        self.init()

    def init(self):
        for i in range(len(self.arr) // 2, -1, -1):
            self.heapify(i, should_heapify_down=True)

    def heapify(self, idx, *, should_heapify_down=False, should_heapify_up=False):
        left_child_idx, right_child_idx = get_child_indices(idx)
        try:
            left_child = self.arr[left_child_idx]
        except IndexError:
            left_child = None
        try:
            right_child = self.arr[right_child_idx]
        except IndexError:
            right_child = None

        if left_child and right_child:
            greater_child_idx = left_child_idx if left_child >= right_child else right_child_idx
        elif left_child:
            greater_child_idx = left_child_idx
        elif right_child:
            greater_child_idx = right_child_idx
        else:
            return

        if self.arr[greater_child_idx] > self.arr[idx]:
            self.arr[idx], self.arr[greater_child_idx] = self.arr[greater_child_idx], self.arr[idx]
            if should_heapify_down:
                self.heapify(greater_child_idx, should_heapify_down=True)
            if should_heapify_up:
                parent_idx = max(get_parent_idx(idx), 0)
                self.heapify(parent_idx, should_heapify_up=True)

    def contains(self, x):
        bt_set = set(self.arr)
        return x in bt_set

    def add(self, x):
        self.arr.append(x)
        idx = len(self.arr) - 1
        parent_idx = get_parent_idx(idx)
        self.heapify(parent_idx, should_heapify_up=True)

    def pop(self):
        last_idx = len(self.arr) - 1
        self.arr[0], self.arr[last_idx] = self.arr[last_idx], self.arr[0]
        value_being_removed = self.arr.pop()
        self.heapify(0, should_heapify_down=True)
        return value_being_removed


h = Heap([5, 6, 1, 2, 12, 17, 9, 4, 8, 23, 16, 7, 19, 21])

h.add(26)
h.add(15)
h.add(-16)

print('h contains 8', h.contains(8))
print('h does not contain 923', not h.contains(923))
# print('h should pop 26', h.pop() == 26)
# print('h should pop 23', h.pop() == 23)
# print('h should pop 21', h.pop() == 21)

h_length = len(h.arr)

for _ in range(h_length):
    print(h.pop())

print(h.arr)

# END TIME: 7:03pm

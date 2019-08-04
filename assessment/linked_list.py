# START TIME: 8:21am


class Node:
    def __init__(self, x):
        self.val = x
        self.next = None


class LL:
    def __init__(self, arr):
        self.list = self.head = self.tail = None
        self.length = 0
        self.init_ll(arr)

    def __repr__(self):
        res = []
        curr = self.list
        while curr:
            res.append(curr.val)
            curr = curr.next
        return str(res)

    def init_ll(self, arr):
        for x in arr:
            if not self.list:
                self.list = self.tail = self.head = Node(x)
                continue
            self.tail.next = Node(x)
            self.tail = self.tail.next
        self.length = len(arr)

    @property
    def size(self):
        return self.length

    def contains(self, x):
        curr = self.list
        while curr:
            if curr.val == x:
                return True
            curr = curr.next
        return False

    def add(self, x):
        self.tail.next = Node(x)
        self.tail = self.tail.next
        self.length += 1

    def remove(self, x):
        curr, prev = self.list, None

        while curr:
            if curr.val == x:
                self.length -= 1

                # if removing first node
                if not prev:
                    self.list = self.list.next
                else:
                    prev.next = curr.next
                return

            if not prev:
                prev = curr
            else:
                prev = curr

            curr = curr.next


ll = LL([1, 2, 3, 4, 5])

# ll_list = ll.list
# while ll_list:
#     print(ll_list.val)
#     ll_list = ll_list.next

print(ll.size)

print('ll should contain 5', ll.contains(5))
print('ll should not contain 8', not ll.contains(8))
print('ll size = 5', ll.size == 5)
print('ll head = 1', ll.head.val == 1)
print('ll tail = 5', ll.tail.val == 5)

ll.add(6)
ll.add(7)

print('ll size = 7', ll.size == 7)
print('ll tail = 5', ll.tail.val == 7)

ll.remove(1)
ll.remove(4)

print('ll removed should not include 1 or 4', ll)

# END TIME: 8:43am

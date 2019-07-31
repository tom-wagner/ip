# START TIME: 7:13am


class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


class LL:
    def __init__(self, arr):
        self.head = self.tail = self.size = None
        self.init_from_arr(arr)

    def __repr__(self):
        res = []
        curr = self.head
        while curr:
            res.append(curr.val)
            curr = curr.next
        return str(res)

    def init_from_arr(self, arr):
        head = tail = None

        for x in arr:
            if head is None:
                head = Node(x)
                tail = head
                continue
            tail.next = Node(x)
            tail = tail.next

        self.head, self.tail, self.size = head, tail, len(arr)

    def contains(self, x):
        curr = self.head

        while curr:
            if curr.val == x:
                return True
            curr = curr.next
        return False

    def add(self, x):
        self.tail.next = Node(x)
        self.tail = self.tail.next
        self.size += 1

    def remove(self, x):
        curr = prev = self.head

        if curr.val == x:
            self.head = self.head.next
            self.size -= 1
            return 'removed'

        while curr:
            if curr.val == x:
                prev.next = curr.next
                self.size -= 1
                return 'removed'
            prev = prev.next if curr != prev else prev
            curr = curr.next


ll = LL([1, 2, 3, 4, 5])

print(ll)

print('ll should contain 5', ll.contains(5))
print('ll should not contain 8', not ll.contains(8))
print('ll size = 5', ll.size == 5)
print('ll head = 1', ll.head.val == 1)
print('ll tail = 5', ll.tail.val == 5)

ll.add(6)
ll.add(7)

print(ll)

print('ll size = 7', ll.size == 7)
print('ll tail = 7', ll.tail.val == 7)

print('ll removed should include 7', ll.contains(7))

print(ll.remove(1))
print(ll.remove(4))

print(ll)

print('ll removed should not include 1 or 4', not ll.contains(1))
print('ll removed should not include 4', not ll.contains(4))

# END TIME: 7:35 AM

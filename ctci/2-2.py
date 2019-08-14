from linked_list import LinkedList


# in place -> O(2n)
def kth_to_last(ll, k):
    curr, ll_length, i = ll.head, 0, 0
    while curr:
        curr = curr.next
        ll_length += 1

    curr = ll.head
    while True:
        if i == ll_length - k - 1:
            return curr
        curr = curr.next
        i += 1

    raise Exception


# with linear space, one pass -> O(n)
def kth_to_last_one_pass(ll, k):
    curr, res = ll.head, []
    while curr:
        res.append(curr)
        curr = curr.next

    return res[len(res) - k - 1]


a = [1, 2, 3, 4, 5]
ll = LinkedList(a)
print(kth_to_last(ll, 2))
print(kth_to_last_one_pass(ll, 2))

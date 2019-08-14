from linked_list import LinkedList


def partition(ll, val):
    curr = divider = ll.head

    while curr:
        print(curr)
        if curr.val < val:
            if curr is divider:
                curr = curr.next
                divider = curr
            else:
                print('flipping: ', curr, divider)
                divider.val, curr.val = curr.val, divider.val
                # divider.next, curr.next = curr.next, divider.next
                print('flipped: ', curr, divider)
                divider = divider.next
                curr = curr.next
        else:
            curr = curr.next
    return ll


a = [3, 5, 8, 5, 10, 2, 1]
ll = LinkedList(a)
print(partition(ll, 4))

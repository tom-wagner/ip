from linked_list import LinkedList


def remove_duplicates(linked_list):
    seen = {linked_list.head.val}
    prev, curr = linked_list.head, linked_list.head.next

    while curr:
        if curr.val in seen:
            prev.next = curr.next
        else:
            seen.add(curr.val)
            prev = prev.next
        curr = curr.next

    return linked_list


a = [1, 2, 3, 4, 2, 5, 6, 4, 7, 8, 4, 3, 2, 9, 8, 1]
ll = LinkedList(a)
print(remove_duplicates(ll))





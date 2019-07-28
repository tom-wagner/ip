import random


def quicksort(arr):
    if len(arr) <= 1:
        return arr

    pivot = arr[0]
    smaller = []
    larger = []

    for idx, val in enumerate(arr):
        if idx == 0:
            continue

        if val < pivot:
            smaller.append(val)
        else:
            larger.append(val)

    return quicksort(smaller) + [pivot] + quicksort(larger)


def dual_pivot(arr):
    if len(arr) <= 1:
        return arr
    elif len(arr) == 2:
        return [arr[0], arr[1]] if arr[0] < arr[1] else [arr[1], arr[0]]

    p1, p2 = arr[0], arr[1]
    sm_pv, lg_pv = (p1, p2) if p2 > p1 else (p2, p1)

    small = []
    med = []
    large = []

    for idx, val in enumerate(arr):
        if idx in {arr[0], arr[1]}:
            continue

        if val <= sm_pv:
            small.append(val)
        elif sm_pv < val < lg_pv:
            med.append(val)
        else:
            large.append(val)

    return dual_pivot(small) + [sm_pv] + dual_pivot(med) + [lg_pv] + dual_pivot(large)

for _ in range(10):
    array = [random.randint(1, 1000000) for _ in range(100000)]
    print(quicksort(array))
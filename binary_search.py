def binary_search(arr, item):
    low = 0
    high = len(arr) - 1

    while low <= high:
        curr_idx = (high + low) // 2
        curr_el = arr[curr_idx]
        if curr_el == item:
            return True
        elif curr_el < item:
            low = curr_idx + 1
        elif curr_el > item:
            high = curr_idx - 1

    return False


# TESTING:
# for x in range(1000):
#     test_arr = list(sorted([random.randint(1, 10000) for _ in range(1000)]))
#     target_int = random.randint(1, 10000)
#     search_res = binary_search(test_arr, target_int)
#     in_set = target_int in set(test_arr)
#     if search_res != in_set:
#         raise Exception

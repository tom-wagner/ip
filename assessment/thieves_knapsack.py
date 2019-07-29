# START TIME: 7:10am

from math import gcd
from functools import reduce
from helpers.thieves_solution import knapsack01_dp, totalvalue

#    item, weight, value
ITEMS = (
    ("map", 9, 150),
    ("compass", 13, 35),
    ("water", 153, 200),
    ("sandwich", 50, 160),
    ("glucose", 15, 60),
    ("tin", 68, 45),
    ("banana", 27, 60),
    ("apple", 39, 40),
    ("cheese", 23, 30),
    ("beer", 52, 10),
    ("suntan cream", 11, 70),
    ("camera", 32, 30),
    ("t-shirt", 24, 15),
    ("trousers", 48, 10),
    ("umbrella", 73, 40),
    ("waterproof trousers", 42, 70),
    ("waterproof overclothes", 43, 75),
    ("note-case", 22, 80),
    ("sunglasses", 7, 20),
    ("towel", 18, 12),
    ("socks", 4, 50),
    ("book", 30, 10),
)

MAX_WT = 400


def greatest_common_factor(items, max_wt):
    weights = [weight for _, weight, _ in items] + [max_wt]
    return reduce(gcd, weights)


def set_up_matrix(items, gcf, max_wt):
    first_row = [x for x in range(0, max_wt + 1, gcf)]

    matrix = []
    for _ in items:
        matrix.append([None for _ in range(0, len(first_row))])
    return matrix, first_row


def get(matrix, row, col):
    try:
        curr = matrix[row][col]
        if curr:
            return curr
    except:
        pass
    return 0, []


def map_weights_to_indexes(weights):
    return {v: k for k, v in enumerate(weights)}


def thieves(items, max_wt):
    gcf = greatest_common_factor(items, max_wt)
    matrix, weights = set_up_matrix(items, gcf, max_wt)

    index_weight_map = map_weights_to_indexes(weights)

    for i, row in enumerate(matrix):
        curr_item, curr_weight, curr_value = items[i]
        for j, _ in enumerate(row):
            max_wt = weights[j]

            prev_max_value_for_weight, prev_max_items = get(matrix, i - 1, j)
            remaining_weight_val, other_items = get(matrix, i - 1, index_weight_map.get(max_wt - curr_weight, 0))
            if curr_weight <= max_wt:
                max_value_if_curr_item_is_kept, items_to_keep = curr_value + remaining_weight_val, other_items + [items[i]]
            else:
                max_value_if_curr_item_is_kept, items_to_keep = 0, []

            if prev_max_value_for_weight > max_value_if_curr_item_is_kept:
                matrix[i][j] = [prev_max_value_for_weight, prev_max_items]
                continue
            matrix[i][j] = [max_value_if_curr_item_is_kept, items_to_keep]

    return matrix[len(matrix) - 1][len(weights) - 1]


max_value, items_to_keep = thieves(ITEMS, MAX_WT)
solution_bagged = knapsack01_dp(ITEMS, MAX_WT)
total_value_solution = totalvalue(solution_bagged)

print('my answer =', items_to_keep)
print('solution =', solution_bagged)
print('total value my items = ', max_value)
print('solution total value =', total_value_solution)
print('correct?', max_value == total_value_solution[0])

# END TIME:

# START TIME: 7:05pm

from helpers.thieves_solution import knapsack01_dp, totalvalue

#    item, weight, value
items = (
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

max_wt = 25


def thieves(options, max_wt):
    items_ct = len(options)
    matrix = [[(0, [])] * (max_wt + 1) for _ in range(items_ct + 1)]
    for i in range(1, items_ct + 1):
        for j in range(1, max_wt + 1):
            current_item, curr_weight, curr_val = items[i - 1]
            prev_max_value_for_weight, prev_items = matrix[i - 1][j]
            extra_space_if_item_kept = max(0, j - curr_weight)
            val_other_items, other_items = matrix[i - 1][extra_space_if_item_kept]
            total_val = val_other_items + curr_val
            if curr_weight <= j - 1 and total_val >= prev_max_value_for_weight:
                    matrix[i][j] = (total_val, other_items + [current_item])
            else:
                matrix[i][j] = (prev_max_value_for_weight, prev_items)

    return matrix[items_ct][max_wt]


thieves_answer = thieves(items, max_wt)
solution_bagged = knapsack01_dp(items, max_wt)
total_value_solution = totalvalue(solution_bagged)


print('my answer =', thieves_answer)
print('solution =', solution_bagged)
print('total value my items = ')
print('solution total value =', total_value_solution)
print('correct?', thieves_answer == solution_bagged)

# END TIME: 7:43pm

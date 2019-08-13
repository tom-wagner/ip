# START TIME: 7:50pm

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

max_wt = 50


def matrix_at(i, j, matrix):
    return (0, []) if i < 0 or j < 0 else matrix[i][j]


def thieves(items, max_wt):
    matrix = [[None for _ in range(0, max_wt + 1)] for _ in items]
    for i, item in enumerate(items):
        curr_item, curr_wt, curr_val = item
        for j in range(0, max_wt + 1):
            prev_max_value_for_weight, prev_items_for_weight = matrix_at(i - 1, j, matrix)
            if curr_wt <= j:
                # matrix[i][j] = max of: 1) curr_item + val remaining space OR 2) prev_max for weight
                remaining_space_value, other_items = matrix_at(i - 1, j - curr_wt, matrix)
                if remaining_space_value + curr_val > prev_max_value_for_weight:
                    matrix[i][j] = (remaining_space_value + curr_val, other_items + [curr_item])
                    continue
            matrix[i][j] = (prev_max_value_for_weight, prev_items_for_weight)
    return matrix[len(items) - 1][max_wt]


def total_value(knapsack):
    return 1000


thieves_answer = thieves(items, max_wt)
thieves_total_value = total_value(thieves_answer)
solution_bagged = knapsack01_dp(items, max_wt)
total_value_solution = totalvalue(solution_bagged)


print('my answer =', thieves_answer)
print('solution =', solution_bagged)
print('total value my items = ')
print('solution total value =', total_value_solution)
print('correct?', thieves_answer == solution_bagged)

# END TIME: 8:04pm

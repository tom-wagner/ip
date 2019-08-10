# START TIME:

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

max_wt = 65


def get_current_max(i, j, matrix):
    if i > 0 and j > 0:
        return matrix[i - 1][j]
    return dict(items=[], val=0)


def get_remaining_weight_items_and_value(i, remaining_weight, matrix):
    if i == 0 or remaining_weight <= 0:
        return [], 0
    return matrix[i - 1][remaining_weight]['items'], matrix[i - 1][remaining_weight]['val']


def thieves(items, max_wt):
    all_weights = list(range(0, max_wt + 1))
    matrix = [[None for _ in all_weights] for _ in items]

    for i, row in enumerate(matrix):
        for j, val in enumerate(row):
            curr_item, curr_weight, curr_value = items[i]
            curr_max_for_wt = get_current_max(i, j, matrix)
            if curr_weight <= j:
                remaining_weight = j - curr_weight
                additional_items, additional_value = get_remaining_weight_items_and_value(i, remaining_weight, matrix)
                if additional_value + curr_value >= curr_max_for_wt['val']:
                    matrix[i][j] = dict(items=additional_items + [curr_item], val=additional_value + curr_value)
                    continue
            matrix[i][j] = curr_max_for_wt
    return matrix[len(matrix) - 1][len(all_weights) - 1]





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

# END TIME:

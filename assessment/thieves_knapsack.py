# START TIME: 1:45pm

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

max_wt = 400


def thieves(items, max_wt):
    weights = range(0, max_wt + 1)
    matrix = [[([], 0, 0) for _ in weights] for _ in items]
    for r, item in enumerate(items):
        curr_item, curr_weight, curr_val = item
        for wt in weights:
            remaining_weight = wt - curr_weight
            if r == 0:
                if remaining_weight >= 0:
                    matrix[r][wt] = ([item], curr_weight, curr_val)
                continue

            prev_items_for_wt, prev_weight, prev_max_val_for_wt = matrix[r - 1][wt]
            if remaining_weight >= 0:
                other_items, other_weight, other_val = matrix[r - 1][remaining_weight]
                if other_val + curr_val >= prev_max_val_for_wt:
                    matrix[r][wt] = (other_items + [item], other_weight + curr_weight, other_val + curr_val)
                    continue

            matrix[r][wt] = (prev_items_for_wt, prev_weight, prev_max_val_for_wt)

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

# END TIME: 2:06pm

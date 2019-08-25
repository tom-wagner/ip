# START TIME: 4:56pm

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


class Square:
    def __init__(self, items, value):
        self.items = items
        self.value = value


def thieves(items, max_wt):
    top_row = [x for x in range(0, max_wt + 1)]
    matrix = [[None for _ in top_row] for _ in items]

    for r, item in enumerate(items):
        item, curr_item_weight, curr_value = item
        for c in top_row:
            if r == 0:
                if curr_item_weight <= c:
                    matrix[r][c] = Square(items=[item], value=curr_value)
                else:
                    matrix[r][c] = Square(items=[], value=0)
                continue

            remaining_weight = c - curr_item_weight
            prev_square_for_weight = matrix[r - 1][c]
            if remaining_weight >= 0:
                extra_space = matrix[r - 1][remaining_weight]
                items_to_keep = extra_space.items + [item]
                if extra_space.value + curr_value >= prev_square_for_weight.value:
                    matrix[r][c] = Square(items=items_to_keep, value=extra_space.value + curr_value)
                    continue

            matrix[r][c] = prev_square_for_weight

    last_square = matrix[len(items) - 1][max_wt]
    return dict(v=last_square.value, items=last_square.items)


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

# END TIME: 5:09pm

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

max_wt = 400


def thieves(items, max_wt):
    return 1000


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
